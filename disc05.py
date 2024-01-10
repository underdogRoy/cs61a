def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(seq)):
        seq[i]=fn(seq[i])
    return seq
def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    "*** YOUR CODE HERE ***"
    list=[]
    for elements in seq:
        if pred(elements) == True:
            list.append(elements)
    return list
def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    result=seq[0]
    for i in range(1,len(seq)):
        result=combiner(result,seq[i])
    return result
def count_palindromes(L):
    """The number of palindromic strings in the sequence of strings
    L (ignoring case).
    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    >>> count_palindromes(["101", "rAcECaR", "much", "wow"])
    3
    """
    result=0
    for i in range(len(L)):
        if L[i].lower()==L[i][::-1].lower():
            result+=1
    return result
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)
t=tree(1, [tree(2), tree(4)])
'''
>>> label(t)
1
>>> t[0]
1
>>> label(branches(t)[0])
2
>>> is_leaf(t[1:][1])
True
>>> [label(b) for b in branches(t)]
[2,4]
>>> branches(tree(5, [t, tree(3)]))[0][0]
1
'''
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 0
    return 1+max([height(b) for b in branches(t)])
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t)
    return label(t)+max([max_path_sum(b) for b in branches(t)])
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t)==x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b,x)
        if path is not None:
            return [label(t)]+path
    return None
def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    return label(t)+sum([sum(sum_tree(b) for b in branches(t))])
def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return True
    sums=[sum_tree(b) for b in branches(t)]
    return all(s==sums[0] for s in sums) and all(balanced(b) for b in branches(t))

def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    >>> print_tree(hailstone_tree(8, 3))
    8
        16
            32
                64
            5
                10
    """
    if h==0:
        return tree(n)
    branches = [hailstone_tree(2*n,h-1)]
    if (n-1)%3==0 and ((n-1)//3)%2==1 and (n-1)//3>1:
        branches += [hailstone_tree((n-1)//3,h-1)]
    return tree(n, branches)

def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)
    helper(0, t)