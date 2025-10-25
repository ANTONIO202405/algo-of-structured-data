# #BinarySearch
# class Node:
#     def __init__(self, value):
#         self.value = value 
#         self.left = None
#         self.right = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, value):
#         new_node = Node(value)
#         if self.root is None:
#             self.root = new_node
#             return True
#         temp = self.root
#         while True:
#             if new_node.value == temp.value:
#                 return False
#             elif new_node.value < temp.value:
#                 if temp.left is None:
#                     temp.left = new_node
#                     return True
#                 temp = temp.left
#             else:
#                 if temp.right is None:
#                     temp.right = new_node
#                     return True 
#                 temp = temp.right
#     def contains(self, value):
#         temp = self.root
#         while True:
#             if temp is None:
#                 return False
#             elif temp.value == value:
#                 return True
#             else:
#                 if value < temp.value:
#                     temp = temp.left
#                 else:
#                     temp = temp.right 

# my_tree = BinarySearchTree()
# my_tree.insert(37)
# my_tree.insert(42)
# my_tree.insert(5)
# print(my_tree.contains(42))
# print(my_tree.contains(66))
# print(my_tree.contains(7))
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)


# RecursiveBinarySearch
class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        elif current_node.value == value:
            return True 
        else:
            if value < current_node.value:
                return self.__r_contains(current_node.left, value)
            else:
                return self.__r_contains(current_node.right, value)
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        elif value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    def __r_delete(self, current_node, value):
        if current_node is None:
            return None
        elif value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left 
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete(current_node.right, sub_tree_min)
        return current_node
    def r_delete(self, value):
        self.__r_delete(self.root, value)
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    
my_tree = BinarySearchTree()
# my_tree.r_insert(23)
# my_tree.r_insert(54)
# my_tree.r_insert(12)
# my_tree.r_insert(44)
# my_tree.r_insert(19)
# my_tree.r_insert(5)
# my_tree.r_insert(37)
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(f"After Deleting 2")
my_tree.r_delete(2)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right)
