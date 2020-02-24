from _local_package import bubble_sort


def binary_search(array, element, high, low=0):
    """
        Search index in list by compare middle value with element
        if element > middle search in right side, else left side.
        List must be sorted first.
    """

    middle = low + (high - low) // 2
    if middle >= low:
        if element == array[middle]:
            return middle
        elif element > array[middle]:
            return binary_search(array, element, middle + 1, high)
        else:
            return binary_search(array, element, 0, middle - 1)
    else:
        return None


if __name__ == "__main__":
    import random

    search_elem = 50
    list_int = [random.randint(-100, 100) for i in range(50)]
    for i, v in enumerate(list_int, 1):
        print(f"{v:4}", sep="  ", end="")
        if i % 10 == 0:
            print()
    length = len(list_int) - 1
    result = binary_search(bubble_sort(list_int), search_elem, length)
    print(f"Element = {search_elem}, index = {result}")
