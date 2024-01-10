def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    def condition(x):
        for i in range(1,n+1):
            if x(i):
                print(i)
        return condition
    
def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def match(n):
        i=0
        num=str(n)
        while i<len(num)-k:
            if num[i]!=num[i+k]:
                return False
            i+=1
        return True
    return match
print(match_k(2)(1010))
            


    
