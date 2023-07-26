def solution(n) -> int:
    """
    Solution: 100%

    :param n: n is an integer within the range [1..2,147,483,647].
    :return: the length of n's longest binary gap
    """
    bin_str = str(bin(n))[2:]
    gap = max_gap = 0
    
    for symbol in bin_str:
        if symbol == '0':
            gap += 1
        else:
            max_gap = max(gap, max_gap)
            gap = 0

    return max_gap
