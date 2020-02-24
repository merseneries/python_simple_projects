def get_digit_input(text):
    while True:
        try:
            tmp = int(input(text))
            break
        except ValueError:
            print("It must be digit.")
    return tmp


def bubble_sort(array):
    arr_len = len(array)

    if arr_len == 0:
        return 0

    for j in range(arr_len):
        for i in range(arr_len - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array
