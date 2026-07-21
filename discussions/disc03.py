def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 0:
        return 1
    else:
        return n * skip_factorial(n-2)

def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    def swipe(n):
        if n < 10:
            print(n)
        else:
            print(n%10)
            swipe(n//10)
            print(n%10)

swipe(123)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def check(d):
        if d*d > n:
            return True
        if n%d == 0:
            return False
        return check(d+1)
    return n >= 2 and check(2)



def hailstone(n):

    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1 + hailstone(n // 2)

def odd(n):
    return 1 + hailstone(3 * n + 1)


hailstone(10)



def sevens(n, k):
    def f(i, who, direction):
        if i == n:
            return who
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        next_who = who + direction
        if next_who > k:
            next_who = 1
        elif next_who < 1:
            next_who = k
        return f(i + 1, next_who, direction)

    return f(1, 1, 1)

# i   who  dir   note
# 1    1   +1
# 2    2   +1
# 3    3   +1
# 4    4   +1
# 5    5   +1
# 6    1   +1   wrapped 6→1
# 7    2   +1
# 8    1   -1   FLIP after 7 (multiple of 7), then step backward 2→1
# 9    5   -1   wrapped 0→5
# 10   4   -1
# 11   3   -1
# 12   2   -1
# 13   1   -1
# 14   5   -1   wrapped 0→5
# 15   1   +1   FLIP after 14 (multiple of 7), then step forward 5→1
# 16   2   +1
# 17   3   +1
# 18   2   -1   FLIP after 17 (has_seven), then step backward 3→2