import operator
from tkinter import *
from functools import partial


class Calculator:
    elements = dict()
    text_elements = [
        ["C", "X", "%", "/"],
        ["7", "8", "9", "x"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["+/-", "0", ".", "="]
    ]
    name_elements = [
        ["clear", "delete", "percent", "divide"],
        ["7", "8", "9", "multiply"],
        ["4", "5", "6", "minus"],
        ["1", "2", "3", "add"],
        ["prefix", "0", "dot", "equal"]
    ]

    def __init__(self, main_window):
        self.text_box = Text(width=25, height=2)
        self.initialization(main_window)
        self.location()
        self.binding()

    def initialization(self, window):
        for name_row, text_row in zip(self.name_elements, self.text_elements):
            for name, text in zip(name_row, text_row):
                self.elements["button_" + name] = Button(window, text=text, width=5, height=2,
                                                         font=("Verdana", 9, "bold"))

    def location(self):
        self.text_box.grid(row=0, column=0, columnspan=4)
        for index_row, name_row in enumerate(self.name_elements, 1):
            for index_column, name in enumerate(name_row):
                self.elements["button_" + name].grid(row=index_row, column=index_column)

    def binding(self):
        except_list = ["C", "X", "+/-", "="]

        for name_row, text_row in zip(self.name_elements, self.text_elements):
            for name, text in zip(name_row, text_row):
                if text in except_list:
                    continue
                send_partial = partial(self.send_character_to_text_box, text)
                self.elements["button_" + name]["command"] = send_partial

        self.elements["button_clear"]["command"] = self.clear
        self.elements["button_delete"]["command"] = self.delete
        self.elements["button_equal"]["command"] = self.equal

    def send_character_to_text_box(self, char):
        self.text_box.insert("end", char)
        self.text_box.tag_add("input_field", 1.0, "1.end")
        self.text_box.tag_config("input_field", font=("Verdana", 20, "bold"), justify=RIGHT)

    def clear(self):
        self.text_box.delete(1.0, "end")

    def delete(self):
        self.text_box.delete("end-2c")

    def equal(self):
        def get_indexes(index_input, operators_input):
            """Get indexes for slice list

            :param index_input:
                List of operator with there indexes.
            :param operators_input:
                List of operators "/, x, +, -"
            :return: start and end index for slice.
            """
            for op in operators_input:
                for i in index_input:
                    if i[0] == op:
                        left = i[1] - 1
                        right = i[1] + 2
                        return left, right

        def simple_calculate(input_list):
            """Get result of operation on two digits

            :param input_list:
                List that contain 2 digits and 1 operator
            :return: digit
            """
            operators = {
                "/": operator.floordiv,
                "x": operator.mul,
                "+": operator.add,
                "-": operator.sub,
            }
            return operators[input_list[1]](input_list[0], input_list[-1])

        def calculation(input_list):
            if len(input_list) < 4:
                return simple_calculate(input_list)

            left_index = right_index = -1
            operators_index = [(v, i) for i, v in enumerate(input_list) if type(v) == str]

            for i in operators_index:
                counter = 0
                if i[0] == "(":
                    left_index = i[1] + 1
                    counter += 1
                    continue
                if i[0] == ")" and counter == 0:
                    right_index = i[1]
                    return calculation(
                        input_list[:left_index - 1] + [calculation(input_list[left_index:right_index])] + input_list[
                                                                                                          (
                                                                                                                      right_index + 1):])
                counter -= 1
            else:
                left_index, right_index = get_indexes(operators_index, ["/", "x", "+" or "-"])

            return calculation(
                input_list[:left_index] + [calculation(input_list[left_index:right_index])] + input_list[right_index:])

        text = self.text_box.get(1.0, "end-1c")
        separated_list = list(filter(None, re.split(r"([()+\-x/])", text)))
        math_list = [int(i) if i.isdigit() else i for i in separated_list]
        result = calculation(math_list)
        self.clear()
        self.send_character_to_text_box(result)

    def addition(self):
        pass

    def substraction(self):
        pass

    def multiplication(self):
        pass

    def division(self):
        pass


root = Tk()
cal = Calculator(root)
root.geometry("203x245")
root.mainloop()
