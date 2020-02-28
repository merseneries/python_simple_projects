import pytest
from binary_search import binary_search


@pytest.mark.parametrize("sorted_list,element",
                         [([0, 10, 20, 30, 40, 50, 54, 100], 200), ([-33.4, -23.34, 0, 11.2, 43.4, 199.6], 5.34)])
def test_sorted_not_in_list(sorted_list, element):
    length = len(sorted_list) - 1
    assert binary_search(sorted_list, element, length) is None


@pytest.mark.parametrize("input_list, element", [([300, 239, 34, -199, 39, -10.4, 39.6, -100], 34),
                                                 (["hello", "grin", "petro", "bye", "angry"], "bye")])
def test_not_sorted_in_list(input_list, element):
    length = len(input_list) - 1
    assert binary_search(input_list, element, length) is None


@pytest.mark.parametrize("sorted_list, element", [([-10.5, -5.0, 1.5, 10, 39, 122, 155.88, 488], -5.0),
                                                  (
                                                  ["angry", "dirol", "free", "make", "priority", "syndrome"], "dirol")])
def test_sorted_in_list(sorted_list, element):
    length = len(sorted_list) - 1
    assert binary_search(sorted_list, element, length) == 1
