class Tree:
    """A tree has a label and a list of branches.

    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        branch_str = ', ' + repr(self.branches) if self.branches else ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ...              Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
    while x:
        levels.append([n.label for n in x])
        x = sum([n.branches for n in x], [])
    return max(levels, key=len)

def long_paths(t, n):
    """Return a list of all paths in t with length at least n.

    >>> long_paths(Tree(1), 0)
    [[1]]
    >>> long_paths(Tree(1), 1)
    []
    >>> t = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5), Tree(6, [Tree(7, [Tree(8)])])])
    >>> print(t)
    1
      2
        3
        4
      5
      6
        7
          8
    >>> for path in long_paths(t, 2):
    ...     print(path)
    ...
    [1, 2, 3]
    [1, 2, 4]
    [1, 6, 7, 8]
    >>> long_paths(t, 3)
    [[1, 6, 7, 8]]
    """
    if t.is_leaf() and n <= 0:
        return [[t.label]]
    paths = []
    for b in t.branches:
        for path in long_paths(b, n - 1):
            paths.append([t.label] + path)
    return paths

def level_mutation(t, funcs):
    """Mutates t using the functions in the list funcs.

    >>> t = Tree(1, [Tree(2, [Tree(3)])])
    >>> funcs = [lambda x: x + 1, lambda y: y * 5, lambda z: z ** 2]
    >>> level_mutation(t, funcs)
    >>> t                               # funcs[0] was applied to the label 1, funcs[1] to the label 2, etc.
    Tree(2, [Tree(10, [Tree(9)])])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> level_mutation(t2, funcs)
    >>> t2                              # (2 * 5) ** 2 = 100
    Tree(2, [Tree(100), Tree(15, [Tree(16)])])
    >>> t3 = Tree(1, [Tree(2)])
    >>> level_mutation(t3, funcs)
    >>> t3
    Tree(2, [Tree(100)])
    """
    if not funcs:
        return
    t.label = funcs[0](t.label)
    remaining = funcs[1:]
    if t.is_leaf() and remaining:
        for f in remaining:
            t.label = f(t.label)
    for b in t.branches:
        level_mutation(b, remaining)

def delete(t, x):
    """Remove all nodes labeled x below the root within Tree t. When a non-leaf
    node is deleted, the deleted node's children become children of its parent.

    The root node will never be removed.

    >>> t = Tree(3, [Tree(2, [Tree(2), Tree(2)]), Tree(2), Tree(2, [Tree(2, [Tree(2), Tree(2)])])])
    >>> delete(t, 2)
    >>> t
    Tree(3)
    >>> t = Tree(1, [Tree(2, [Tree(4, [Tree(2)]), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(4)])
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(2, [Tree(6),  Tree(2), Tree(7), Tree(8)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(6), Tree(7), Tree(8), Tree(4)])
    """
    new_branches = []
    for b in t.branches:
        delete(b, x)
        if b.label == x:
            new_branches.extend(b.branches)
        else:
            new_branches.append(b)
    t.branches = new_branches
