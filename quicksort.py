def swap(mylist, index1, index2):
    temp = mylist[index1]
    mylist[index1] = mylist[index2]
    mylist[index2] = temp
    return mylist

def pivot(mylist, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist, swap_index, i)
    swap(mylist, pivot_index, swap_index)
    return swap_index


def quicksort(mylist, left, right):
    if left < right:
        pivot_index = pivot(mylist, left, right)
        quicksort(mylist, left, pivot_index-1)
        quicksort(mylist,  pivot_index+1, right)
    return mylist

mylist = [4,6,1,7,3,2,5]

print(quicksort(mylist, 0, len(mylist)-1))

#time  complexity

#best case and avg case o(nlogn)
#worst case o(n2)  (when list is already sorted)