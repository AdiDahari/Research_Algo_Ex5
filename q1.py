import doctest
from numbers import Number
from itertools import combinations, accumulate


def bounded_subsets(S, C):
    '''

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

    if not isinstance(C, Number) or \
            not all((isinstance(x, Number) and x >= 0) for x in S) or \
            not C or not S:
        yield []
        return

    S = list(filter(lambda x: x <= C, S))

    S = sorted(S)

    try:
        size = next(
            index for index, x in enumerate(accumulate(S)) if x > C) + 1
    except:
        size = len(S) + 1

    for i in range(size):
        for comb in combinations(S, i):
            if sum(comb) <= C:
                yield list(comb)
            else:
                continue


def sorted_by_sum_bounded_subsets(S, C):
    '''
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
    yield from sorted(bounded_subsets(S, C), key=sum)


if __name__ == '__main__':
    doctest.testmod()
