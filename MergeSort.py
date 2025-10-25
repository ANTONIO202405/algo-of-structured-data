# def merge(l1, l2, l3):
#     for i in l1:
#         for j in l2:
#             if j < i and j not in l3:
#                 l3.append(j)
#                 continue
#             if i < j and i not in l3:
#                 l3.append(i)
#     if len(l1) > 0:
#         for i in l1:
#             if i not in l3:
#                 l3.append(i)
#     if len(l2) > 0:
#         for j in l2:
#             if j not in l3:
#                 l3.append(j)
#     return l3
# print(merge([100, 300, 400], [50, 74, 500], []))

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[ : mid_index])
    right = merge_sort(my_list[mid_index : ])
    return merge(left, right)

print(merge_sort(([3, 8, 2, 1])))
