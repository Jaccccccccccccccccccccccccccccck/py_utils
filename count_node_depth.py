def count_ancestor(node, ancestor_count):
    if not node:
        return
    else:
        print(node.key, ancestor_count)
    if node.left:
        count_ancestor(node.left, ancestor_count + 1)
    if node.right:
        count_ancestor(node.right, ancestor_count + 1)


def count_descendant(node, descendant_count):
    if not node:
        return 0
    else:
        descendant_count = 1 + count_descendant(node.left, descendant_count) + count_descendant(node.right,
                                                                                                descendant_count)
        print(node.key, descendant_count - 1)
        return descendant_count


def node_count_for_each_tree_depth(node, depth, depth_count_list):
    if not node:
        return
    depth_count_list[depth] += 1
    node_count_for_each_tree_depth(node.left, depth + 1, depth_count_list)
    node_count_for_each_tree_depth(node.right, depth + 1, depth_count_list)


def get_height(node):
    if not node:
        return 0
    height_left = get_height(node.left)
    height_right = get_height(node.right)
    if height_left >= height_right:
        return height_left + 1
    else:
        return height_right + 1


def node_count_for_each_tree_height(node, height_count_list):
    if not node:
        return
    height_count_list[get_height(node) - 1] += 1
    if node.left:
        node_count_for_each_tree_height(node.left, height_count_list)
    if node.right:
        node_count_for_each_tree_height(node.right, height_count_list)


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


root = BinaryTree('root')
left_node = BinaryTree('root_left')
left_left_node = BinaryTree('root_left_left')
left_right_node = BinaryTree('root_left_right')
root.left = left_node
left_node.left = left_left_node
left_node.right = left_right_node

# count_ancestor(root, 0)
#
# count_descendant(root, 0)
#
depth_count_list = [0, 0, 0, 0]
node_count_for_each_tree_depth(root, 0, depth_count_list)
print(depth_count_list)

# height_count_list = [0,0,0,0]
# node_count_for_each_tree_height(root, height_count_list)
# print(height_count_list)
