class A():
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return self.x
    def __str__(self):
        return self.x * 2
class B():
    def __init__(self):
        print("boo!")
        self.a = []
    def add_a(self, a):
        self.a.append(a)
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret


def sum_nums(lnk):
    result=0
    while lnk!=Link.empty:
        result+=lnk.first
        lnk=lnk.rest
    return result

def multiply_lnks(lst_of_lnks):
    result=1
    for i in range(len(lst_of_lnks)):
        if lst_of_lnks[i]==Link.empty or lst_of_lnks[i].first==0:
            return Link.empty
        result,lst_of_lnks[i]=result*lst_of_lnks[i].first,lst_of_lnks[i].rest
    first,rest=result,multiply_lnks(lst_of_lnks)
    return Link(first,rest)

def flip_two(lnk):
    if lnk.rest==Link.empty or lnk==Link.empty:
        return
    else:
        lnk.first,lnk.rest.first=lnk.rest.first,lnk.first
        return flip_two(lnk.rest.rest)
    
#with iteration
'''
def filter_link(link,f):
    while link!=Link.empty:
        if f(link.first):
            yield link.first
        link=link.rest
'''
#without iteration
def filter_link(link,f):
    if link==Link.empty:
        return
    elif f(link.first) and link!=Link.empty:
        yield link.first

    yield from filter_link(link.rest,f)

   
def make_even(t):        
    if t.label%2==1:
        t.label+=1
    elif t.is_leaf()==True:
        return
    for b in t.branches:
        make_even(b)

def square_tree(t):
    assert isinstance(t.label,int)
    t.label=t.label**2
    if t.is_leaf()==True:
        return
    for b in t.branches:
        square_tree(b)

def find_paths(t,entry):
    paths=[]
    if t.is_leaf()==True and t.label!=entry:
        return []
    elif t.label==entry:
        return [[entry]]
    else:
        for b in t.branches:
            temp = find_paths(b, entry)
            for lst in temp:
                lst = [t.label] + lst
                paths.append(lst)
        return paths

def combine_tree(t1, t2, combiner):
    if t1.is_leaf():
        return Tree(combiner(t1.label,t2.label))
    else:
        return Tree(combiner(t1.label, t2.label), [combine_tree(t1.branches[i], t2.branches[i], mul) for i in range(len(t1.branches))])



def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    def helper(t,map_fn,level):
        if level:
            t.label = map_fn(t.label)
        level = not level
        if t.is_leaf():
            return Tree(t.label)
        else:
            return Tree(t.label, [helper(b, map_fn, level) for b in t.branches])
    return helper(t,map_fn,True)


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
#a = Tree(1, [Tree(2, [Tree(3)])])
#b = Tree(4, [Tree(5, [Tree(6)])])
#def mul(a,b):
#    return a*b
#t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
#negate = lambda x: -x

