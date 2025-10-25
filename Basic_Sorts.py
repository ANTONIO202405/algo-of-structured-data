# def bubble_sort(my_list):
#     for i in range(len(my_list) - 1, 0, -1):
#         for j in range(i):
#             if my_list[j] > my_list[j+1]:
#                 temp = my_list[j]
#                 my_list[j] = my_list[j + 1]
#                 my_list[j + 1] = temp
#     return my_list

# print(bubble_sort([16, 72, 48, 89, 60, 55]))

# def selection_sort(my_list):
#     for i in range(0, len(my_list) - 1):
#         min_value =  i
#         for j in range(i + 1, len(my_list)):
#             if my_list[j] < my_list[min_value]:
#                 min_value = j
#         if i != min_value:
#             temp = my_list[i]
#             my_list[i] = my_list[min_value]
#             my_list[min_value] = temp
#     return my_list
# print(selection_sort([16, 72, 48, 89, 60, 55]))

# def insertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         while my_list[i] < my_list[i - 1] and i > 0:
#             temp = my_list[i - 1]
#             my_list[i - 1] = my_list[i]
#             my_list[i] = temp
#             i = i - 1
#     return my_list
# print(insertion_sort([16, 72, 48, 89, 60, 55]))
# print(insertion_sort([5, 4, 3, 2, 1]))


