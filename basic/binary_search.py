import random
from _local_package import bubble_sort


def binary_search(array, element, high, low=0):
    """
        Search index in list by compare middle value with element
        if element > middle search in right side, else left side.
        List must be sorted first.
    """
    if high >= low:
        middle = low + (high - low) // 2
        if element == array[middle]:
            return middle
        elif element > array[middle]:
            return binary_search(array, element, high, middle + 1)
        else:
            return binary_search(array, element, middle - 1, low)
    else:
        return None


if __name__ == "__main__":
    search_elem = 66
    list_int = [random.randint(-100, 100) for i in range(50)]
    for i, v in enumerate(bubble_sort(list_int), 1):
        print(f"{v:4}", sep="  ", end="")
        if i % 10 == 0:
            print()
    length = len(list_int) - 1
    result = binary_search(list_int, search_elem, length)
    print(f"Element = {search_elem}, index = {result}")
