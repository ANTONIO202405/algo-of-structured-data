# Tree
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while True:
            if temp is None:
                return False
            if value < temp.value:
                temp = temp.left
                continue
            if value > temp.value:
                temp = temp.right
                continue
            if value == temp.value:
                return True

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(7)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(7))



# Binary Search Tree
# Recurssion
# Tree Traversal


