import pytest
from sorts.bubble_sort import bubble_sort_iterative, bubble_sort_recursive

@pytest.mark.parametrize("sort_function", [bubble_sort_iterative, bubble_sort_recursive])
def test_bubble_sort(sort_function):
    assert sort_function([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]
    assert sort_function([1]) == [1]
    assert sort_function([]) == []
    assert sort_function([-2, -45, -5]) == [-45, -5, -2]
    assert sort_function([-23, 0, 6, -4, 34]) == [-23, -4, 0, 6, 34]
    assert sort_function(['d', 'a', 'b', 'e']) == ['a', 'b', 'd', 'e']
    assert sort_function(['z', 'a', 'y', 'b', 'x', 'c']) == ['a', 'b', 'c', 'x', 'y', 'z']
    assert sort_function([1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6]) == [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
    assert sort_function([1, 3.3, 5, 7.7, 2, 4.4, 6]) == [1, 2, 3.3, 4.4, 5, 6, 7.7]

# Edge case: Testing large list
@pytest.mark.parametrize("sort_function", [bubble_sort_iterative, bubble_sort_recursive])
def test_bubble_sort_large(sort_function):
    import random
    large_list = random.sample(range(-1000, 1000), 200)  # Random 200 unique numbers
    assert sort_function(large_list) == sorted(large_list)