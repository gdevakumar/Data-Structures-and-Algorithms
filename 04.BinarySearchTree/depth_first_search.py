from binarysearchtree import BinarySearchTree


def pre_order(tree):
    results = []
    def traverse(node):
        results.append(node.value)
        if node.left is not None:
            traverse(node.left)
        if node.right is not None:
            traverse(node.right)
        return results
    return traverse(tree.root)

def in_order(tree):
    results = []
    def traverse(node):
        if node.left:
            traverse(node.left)
        results.append(node.value)
        if node.right:
            traverse(node.right)
        return results
    return traverse(tree.root)

def post_order(tree):
    results = []
    def traverse(node):
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)
        results.append(node.value)
        return results
    return traverse(tree.root)


my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

"""
                 47
               /    \
             21      76
            /  \    /  \
          18   27  52   82
"""

print("Pre Order")
print(pre_order(my_tree))

print("\nIn Order")
print(in_order(my_tree))

print("\nPost Order")
print(post_order(my_tree))
