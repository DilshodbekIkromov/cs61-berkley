def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    prev = next(t)
    for x in t:
        yield x - prev
        prev = x

def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.
    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        for rest in partition_gen(n - m, m):
            yield rest + ' + ' + str(m)
    if m > 1:
        yield from partition_gen(n, m - 1)



def squares(total, k):
    """Yield the ways in which perfect squares greater or equal to k*k sum to total.

    >>> list(squares(10, 1))  # All lists of perfect squares that sum to 10
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1], [4, 4, 1, 1], [9, 1]]
    >>> list(squares(20, 2))  # Only use perfect squares greater or equal to 4 (2*2).
    [[4, 4, 4, 4, 4], [16, 4]]
    """
    assert total > 0 and k > 0
    if total == k * k:
        yield [k * k]
    elif total > k * k:
        for s in squares(total - k * k, k):
            yield s + [k * k]
        yield from squares(total, k + 1)


def church_generator(f):
    """Takes in a function f and yields functions which apply f
    to their argument one more time than the previously generated
    function.

    >>> increment = lambda x: x + 1
    >>> church = church_generator(increment)
    >>> for _ in range(5):
    ...     fn = next(church)
    ...     print(fn(0))
    0
    1
    2
    3
    4
    """

    g = lambda x: x
    while True:
        yield g
        g = (lambda prev: lambda x: f(prev(x)))(g)