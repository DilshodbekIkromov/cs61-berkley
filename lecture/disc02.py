def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def f(cond):
        a = 0 
        while a <= n: 
            if cond(a):
                print(a)
            a +=1 
    return f 

def is_even(x): 
    return x % 2 ==0

make_keeper(5)(is_even)
    

def ramp(n):
    """Return whether non-negative integer N has more increases than decreases.

    >>> ramp(123)   # 2 increases (1-> 2, 2-> 3) and 0 decreases
    True
    >>> ramp(1315)  # 2 increases (1-> 3, 1-> 5) and 1 decrease (3-> 1)
    True
    >>> ramp(176)   # 1 increase (1-> 7) and 1 decrease (7-> 6)
    False
    >>> ramp(5)     # 0 increases and 0 decreases
    False
    """
    n, last, tally = n //10 , n%10, 0

    while n:
        n, last, tally = n // 10, n % 10, tally + sign(last - n%10)
    return tally



