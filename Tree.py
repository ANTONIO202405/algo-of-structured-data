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
    def BSF(self):
        queue = []
        result = []
        current_node = self.root
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)        
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result
    def dfs_pre_order(self):
        result = []
        
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
    def dfs_post_order(self):
        result = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result
    
    def dfs_in_order(self):
        result = []
        
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return result
    def is_valid_bst(self):
        results = self.dfs_in_order()
        current_node = results[0]
        for i in results:
            if i < current_node:
                return False
            else:
                current_node = i
        return True
    def kth_smallest(self, num):
        stack = []
        result = []
        if self.root:
            current_node = self.root
        else:
            return None
        if num == 0:
            return None
        while len(result) != num:
            if current_node is None:
                return None
            if len(result) and len(stack) is None:
                return None
            if current_node not in stack:
                stack.append(current_node)
            if current_node.left and current_node.left not in result:
                current_node = current_node.left
            else:
                result.append(current_node)
                stack.pop()
                if current_node.right is None and len(stack) > 0:
                    current_node = stack[-1]
                else:
                    current_node = current_node.right
            
        return result[-1].value
    






my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
# print(my_tree.BSF())
# print(my_tree.dfs_pre_order())
# print(my_tree.dfs_post_order())
# print(my_tree.dfs_in_order())
print(my_tree.kth_smallest(0))
# print(my_tree.is_valid_bst())
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
# print(my_tree.contains(7))



# Binary Search Tree
# Recurssion
# Tree Traversal



