import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from DictsOrganizations.BalancedTree import BalancedTreeNode
from DictsOrganizations.BalancedTree import AVLTree


class TestBalancedTree(unittest.TestCase):
    def setUp(self):
        self.common_AVLtree = AVLTree()
        root = self.common_AVLtree.root
        self.common_AVLtree.add_node(BalancedTreeNode(root, "Lenovo", 70000))
        self.common_AVLtree.add_node(BalancedTreeNode(root, "Toshiba", 65000))
        self.common_AVLtree.add_node(BalancedTreeNode(root, "Philips", 50000))
        self.common_AVLtree.add_node(BalancedTreeNode(root, "Vaio", 90000))
        self.common_AVLtree.add_node(BalancedTreeNode(root, "Samsung", 80000))
        self.common_AVLtree.add_node(BalancedTreeNode(root, "Dell", 85000))
        self.common_AVLtree.add_node(BalancedTreeNode(root, "Apple", 100000))
        self.common_AVLtree.add_node(BalancedTreeNode(root, "HP", 70000))
        self.common_AVLtree.add_node(BalancedTreeNode(root, "Acer", 75000))

    def test_add_node(self):
        current = self.common_AVLtree.root
        self.assertEquals(len(self.common_AVLtree.nodes_list), 9)
        self.assertEquals(current.key, "Philips")
        self.assertEquals(current.value, 50000)
        self.assertEquals(current.left.key, "Dell")
        self.assertEquals(current.right.key, "Toshiba")
        self.assertEquals(current.left.value, 85000)
        self.assertEquals(current.right.value, 65000)
        current = current.left.left
        self.assertEquals(current.key, "Apple")
        self.assertEquals(current.left.key, "Acer")
        self.assertEquals(current.right, None)
        current = self.common_AVLtree.root.right.left
        self.assertEquals(current.key, "Samsung")
        self.assertEquals(current.right, None)
        self.assertEquals(current.left, None)
        self.assertEquals(len(self.common_AVLtree.nodes_list), 9)

    def test_remove(self):
        self.common_AVLtree.remove("Acer")
        self.assertEquals(self.common_AVLtree.root.left.left.left, None)
        self.common_AVLtree.remove("Toshiba")
        self.assertEquals(self.common_AVLtree.root.right.key, "Vaio")
        self.assertEquals(self.common_AVLtree.root.right.left.key, "Samsung")


if __name__ == "__main__":
    unittest.main()
