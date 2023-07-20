from binarysearchtree import BinarySearchTree


def BFS(tree):
    queue = [tree.root]
    result = []
    while len(queue) > 0:
        curr_node = queue.pop(0)
        result.append(curr_node.value)
        if curr_node.left is not None:
            queue.append(curr_node.left)
        if curr_node.right is not None:
            queue.append(curr_node.right)
    return result


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

bfs_order = BFS(my_tree)

print(bfs_order)

