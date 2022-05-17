HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    i=n
    def f(i,term):
        def helper(i,term):
            return f(i-1,term)+term(i)
        if i==1:
            return term(i)
        else:
            return helper(i,term)
        

    return f(n,term)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    def helper(m,n):
        if m==1 or n==1:
            return 1
        elif m==2 and n==2 :
            return 2
        else:
            return paths(m-1,n)+paths(m,n-1)
    return helper(m,n)


def pascal(row, c):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    if c<0 or row<0:
        return 
    elif c>row+1:
        return 0
    elif c==0:
        return 1
    elif c==row:
        return 1

    def helper(m,n):
        if m==0 and n==0:
            return 1
        else:
            return pascal(m-1,n)+pascal(m-1,n-1)

    return helper(row,c)
