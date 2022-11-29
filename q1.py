import doctest
from numbers import Number
from itertools import combinations, accumulate


def bounded_subsets(S, C):
    '''
    This function returns a iterator that yields all subsets of S that sum to C or less.

    TESTS:
    >>> for s in bounded_subsets([1, 2, 3], 4):
    ...     print(s, end=" ")
    [] [1] [2] [3] [1, 2] [1, 3] 
    >>> for s in bounded_subsets(range(50, 150), 103):
    ...     print(s, end=" ")
    [] [50] [51] [52] [53] [54] [55] [56] [57] [58] [59] [60] [61] [62] [63] [64] [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78] [79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90] [91] [92] [93] [94] [95] [96] [97] [98] [99] [100] [101] [102] [103] [50, 51] [50, 52] [50, 53] [51, 52] 
    >>> for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
    ...     print(s, end=" ")
    (0, []) (1, [0]) (2, [1]) (3, [2]) (4, [3]) 
    >>> for s in bounded_subsets(range(2, 100), 1):
    ...     print(s, end=" ")
    [] 
    >>> for s in bounded_subsets([], 1000000000000):
    ...     print(s, end=" ")
    [] 
    >>> for s in bounded_subsets([1, 2, 3, 4, 5], 15):
    ...     print(s, end=" ")
    [] [1] [2] [3] [4] [5] [1, 2] [1, 3] [1, 4] [1, 5] [2, 3] [2, 4] [2, 5] [3, 4] [3, 5] [4, 5] [1, 2, 3] [1, 2, 4] [1, 2, 5] [1, 3, 4] [1, 3, 5] [1, 4, 5] [2, 3, 4] [2, 3, 5] [2, 4, 5] [3, 4, 5] [1, 2, 3, 4] [1, 2, 3, 5] [1, 2, 4, 5] [1, 3, 4, 5] [2, 3, 4, 5] [1, 2, 3, 4, 5] 
    '''
    # C is not a number OR
    # one or more of the elements in S are not numbers OR
    # one or more of the elements in S are negative OR
    # C or S are empty
    if not isinstance(C, Number) or \
            not all((isinstance(x, Number) and x >= 0) for x in S) or \
            not C or not S:
        yield []
        return

    # S is now a list of numbers that are all positive and lower or equal to C
    S = list(filter(lambda x: x <= C, S))

    # S is being sorted
    S = sorted(S)

    try:
        # Checking for the size of the biggest subset possible
        size = next(
            index for index, x in enumerate(accumulate(S)) if x > C) + 1
    except:
        # default size is the size of S
        size = len(S) + 1

    for i in range(size):
        # Using combinations to get all possible subsets of size i
        for comb in combinations(S, i):
            # Checking if the sum of the subset is lower or equal to C
            if sum(comb) <= C:
                # Yielding the subset
                yield list(comb)
            else:
                # If the sum is bigger than C, there is no need to check the rest of the subsets
                continue


def sorted_by_sum_bounded_subsets(S, C):
    '''
    This function returns a iterator that yields all subsets of S that sum to C or less, sorted by the sum of the subsets.

    TESTS:
    >>> for s in sorted_by_sum_bounded_subsets([5, 6, 7, 8], 4):
    ...     print(s, end=" ")
    [] 
    >>> for s in sorted_by_sum_bounded_subsets([], 4):
    ...     print(s, end=" ")
    [] 
    >>> for s in sorted_by_sum_bounded_subsets([1, 2, 3], 4):
    ...     print(s, end=" ")
    [] [1] [2] [3] [1, 2] [1, 3] 
    >>> for s in sorted_by_sum_bounded_subsets(range(50, 150), 103):
    ...     print(s, end=" ")
    [] [50] [51] [52] [53] [54] [55] [56] [57] [58] [59] [60] [61] [62] [63] [64] [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78] [79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90] [91] [92] [93] [94] [95] [96] [97] [98] [99] [100] [101] [50, 51] [102] [50, 52] [103] [50, 53] [51, 52] 
    '''
    # Yielding the subsets sorted by the sum of the subsets by the previous function result, sorting by sum function
    yield from sorted(bounded_subsets(S, C), key=sum)


if __name__ == '__main__':
    doctest.testmod()
