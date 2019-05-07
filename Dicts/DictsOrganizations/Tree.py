class TreeNode():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def init_node(self, left, right):
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.nodes_list = []
        self.root = None

    def add_node(self, new_node):
        current_node = TreeNode(new_node.key, new_node.value)
        if self.root is None:
            self.root = current_node
            self.nodes_list.append(current_node)
        else:
            parent_item = self.root
            while (parent_item.left is not None
                   and new_node.key < parent_item.key) \
                or (parent_item.right is not None
                    and new_node.key > parent_item.key):
                if new_node.key < parent_item.key:
                    parent_item = parent_item.left
                else:
                    parent_item = parent_item.right
            if new_node.key < parent_item.key:
                parent_item.init_node(current_node, parent_item.right)
            else:
                parent_item.init_node(parent_item.left, current_node)
            current_node.parent = parent_item
            self.nodes_list.append(current_node)

    def search(self, root, needed_key):
        while True:
            if root is None:
                return None
            if root.key < needed_key:
                root = root.right
            elif root.key > needed_key:
                root = root.left
            else:
                return root

    def get_min(self, root):
        minimum = TreeNode()
        while root.left is not None:
            root = root.left
        return minimum

    def remove(self, element):
        if element in self.nodes_list:
            self.nodes_list.remove(element)
            element_parent = element.parent
            if element_parent is not None:
                if element.right is None and element.left is None:
                    if element_parent.left == element:
                        element_parent.left = None
                    if element_parent.right == element:
                        element_parent.right = None
                elif element.right is None or element.left is None:
                    if element.left is None:
                        if element_parent.left == element:
                            element_parent.left = element.right
                        else:
                            element_parent.right = element.right
                        element.right.parent = element_parent
                    else:
                        if element_parent.left == element:
                            element_parent.left = element.left
                        else:
                            element_parent.right = element.left
                        element.left.parent = element_parent
            else:
                min_element = self.get_min(element)
                if min_element.right is None:
                    element = min_element
                    min_element = None
                else:
                    min_element.right.parent = min_element.parent
                    element = min_element
