def sum_digits(n):
    """
    returns sum of digits but computes with recursion
    """
    if not n: 
        return 0 
    return n%10 + sum_digits(n//10)

def count_chars(s, c):
    """
    how many c appears in s 
    >>> count_chars("banana", "a")
    3
    """
    if not s:
        return 0 
    return (1 if s[0]==c else 0) + count_chars(s[1:], c)


def gcd(a,b):
    """
    returns gcd of 2 numbers 
    >>> gcd(2,6)
    2
    >>> gcd(6,11)
    1
    """
    if b == 0: 
        return a 
    return gcd(a, a%b)

def is_pal(s:str):
    """
    checks wether it is palindrome or not
    >>> is_pal("hello")
    False
    >>> is(pal("kiyik")
    True 
    """
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return is_pal(s[1:-1])


def climb(n, memo=None):
    """
    you can take 1 or 2 steps, how many ways you can climb to n step stairs
    >>> climb(5)
    8

    """
    if memo is None:
        memo = {}
    if n <= 2:
        return n 
    if n in memo:
        return memo[n]
    memo[n] = climb(n-1,memo) + climb(n-2,memo)
    return memo[n]


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

root = TreeNode(1, TreeNode(2,TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))

def tree_sum(node):
    if node is None:
        return 0 
    return node.val + tree_sum(node.left) + tree_sum(node.right)

tree_sum(root)

def max_depth(node):
    if node is None:
        return 0 
    return 1 + max(max_depth(node.left), max_depth(node.right))

max_depth(root)

def count_leaves(node):
    if node is None:
        return 0 
    if node.left is None and node.right is None:
        return 1 
    return count_leaves(node.left) + count_leaves(node.right)

count_leaves(root)

def count_nodes(node):
    if node is None:
        return 0 
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def letter_combos(digits):
    if not digits:
        return []
    mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
               '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    result = []
    def backtrack(idx, path):
        if idx == len(digits): 
            result.append(path)
            return
        for ch in mapping[digits[idx]]:
            backtrack(idx + 1, path + ch)
    backtrack(0, "")
    return result

len(letter_combos("23")) 




def total_n_queens(n):
    count = 0
    cols, diag1, diag2 = set(), set(), set() 
    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue # PRUNE: this square is attacked
            cols.add(col); diag1.add(row - col); diag2.add(row + col) # CHOOSE
            backtrack(row + 1)
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col) # UNDO
    backtrack(0)
    return count

total_n_queens(4)
total_n_queens(8) 












