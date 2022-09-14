"""


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


def mergesort(my_list):
    if len(my_list)  == 1:
        return my_list
    mid = int(len(my_list)d/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(mergesort(left), mergesort(right))

print(mergesort([3,1,4,5,2]))

# space complexity  0(n)
# time complexity  0(nlogn)


"""

https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/