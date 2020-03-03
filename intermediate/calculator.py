from tkinter import *


class Calculator:
    constructor = dict()
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
        ["prefix", "0", "dot", "result"]
    ]

    def __init__(self, main_window):
        self.text_box = Text(width=25, height=2)
        self.initialization(main_window)
        self.location()
        self.constructor["button_1"]["command"] = self.press_digit

    def initialization(self, window):
        for name_row, text_row in zip(self.name_elements, self.text_elements):
            for name, text in zip(name_row, text_row):
                self.constructor["button_" + name] = Button(window, text=text, width=5, height=2)

    def location(self):
        self.text_box.grid(row=0, column=0, columnspan=4)
        for index_row, name_row in enumerate(self.name_elements, 1):
            for index_column, name in enumerate(name_row):
                self.constructor["button_" + name].grid(row=index_row, column=index_column)

        # self.button_clear = Button(main_window, text="C").grid(row=1, column=0)
        # self.button_delete = Button(main_window, text="X").grid(row=1, column=1)
        # self.button_percent = Button(main_window, text="%").grid(row=1, column=2)
        # self.button_divide = Button(main_window, text="/").grid(row=1, column=3)

        # self.button_7 = Button(main_window, text="7")
        # self.button_8 = Button(main_window, text="8")
        # self.button_9 = Button(main_window, text="9")
        # self.button_multiply = Button(main_window, text="x")
        #
        # self.button_4 = Button(main_window, text="4")
        # self.button_5 = Button(main_window, text="5")
        # self.button_6 = Button(main_window, text="6")
        # self.button_minus = Button(main_window, text="-")
        #
        # self.button_1 = Button(main_window, text="1")
        # self.button_2 = Button(main_window, text="2")
        # self.button_3 = Button(main_window, text="3")
        # self.button_add = Button(main_window, text="+")
        #
        # self.button_prefix = Button(main_window, text="+/-")
        # self.button_0 = Button(main_window, text="0")
        # self.button_dot = Button(main_window, text=".")
        # self.button_result = Button(main_window, text="=")

    def press_digit(self):
        self.text_box.insert(1.0, "1")

    def addition(self):
        pass

    def substraction(self):
        pass

    def multiplication(self):
        pass

    def division(self):
        pass


main_window = Tk()
cal = Calculator(main_window)
main_window.geometry("202x250")
main_window.mainloop()
