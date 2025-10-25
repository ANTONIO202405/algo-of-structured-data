'''
nums = [2, 1, 2, 7, 11, 15]
target = 9
my_dict = {}
result = []

for i, num in enumerate(nums):
    diff = target - num
    if diff in my_dict:
        # Found the pair!
        result = [my_dict[diff], i]
        break
    # Only add to dict *after* checking to avoid missing second occurrence
    my_dict[num] = i

print(result)
'''

'''
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7
result =[]
set2 = set(arr2)
for i in arr1:
    num = target - i
    if num in set2:
        result.append((i,num))
print(result)
'''

'''
arr = [100, 4, 200, 1, 3, 2]
set1 = set(arr)
length = 1
for i in arr:
    if i + 1 in set1:
        length += 1
    else:
        continue
print(length)
'''
'''
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i} : {val}")
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = HashTable()
my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("nuts", 1500)
my_hash_table.set_item("nail", 1000)
my_hash_table.set_item("washers", 1200)
my_hash_table.print_table()
print(my_hash_table.get_item("washers"))
print(my_hash_table.get_item("bolts"))
print(my_hash_table.get_item("screwdrivers"))
print(my_hash_table.keys())
'''
'''
def first_non_repeating_char(string):
    my_dict = {}
    for i in string:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 0
    print(my_dict)
    for key, value in my_dict.items():
        if value == 0:
            return key
        
        
print(first_non_repeating_char("aabbcc"))
print(first_non_repeating_char("leetcode"))
'''
'''
def find_pairs(arr1, arr2, target):
    pairs = []
    for i in set(arr1):
        if target - i in arr2:
            pairs.append((i, target - i))
    return sorted(pairs)

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

print(find_pairs(arr1, arr2, target))
'''

# # factiorial
# def factorial(num):
#     result = 1
#     while num != 1:
#         result = result * num
#         num -= 1
#     return result
# print(factorial(5))

#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             self.length = 1
#         self.tail.next = new_node
#         self.tail = new_node
#         self.length += 1
#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.value)
#             temp = temp.next
#     def selection_sort(self):
#         pre = self.head
#         for i in range(0, self.length - 1):
#
#             # if self.length < 2:
#             #   return "empty"
#
#             min_value = pre
#             temp = min_value.next
#             while temp:
#                 if temp.value < min_value.value:
#                     min_value = temp
#                 temp = temp.next
#             if min_value != pre and temp:
#                 store = pre.value
#                 pre.value = min_value.value
#                 min_value.value = store
#             pre = pre.next
#         return True
#
#
# my_ll = LinkedList(4)
# my_ll.append(2)
# my_ll.append(6)
# my_ll.append(5)
# my_ll.append(1)
# my_ll.append(3)
# my_ll.selection_sort()
# my_ll.print_list()
#
# print(1,2,3,4)

# def find_longest_string(string_list):
#     longest = ""
#     for i in string_list:
#         if len(i) > len(longest):
#             longest = i
#     return longest
#
# print(find_longest_string(['apple', 'banana', 'kiwi', 'pear']))

# def remove_duplicates(nums):
#     temp = 0
#     while temp != len(nums) - 1:
#         if nums[temp] == nums[temp + 1]:
#             nums[temp] = nums[temp + 1]
#         else:
#             temp += 1
#     return len(nums)
#
#
# print(remove_duplicates([1, 1, 1, 1, 1]))

l = [5, 3, 6, 2, 5]
l[0] = None
print(len(l))
print(l)