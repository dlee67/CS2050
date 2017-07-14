numbers = [17, 41, 5, 22, 54, 6, 29, 3, 13]

#Is this... what they call the legendary multi line commenting....?...!
'''
User passes in a list into the argument.
'''


#0 stands for the low index of the passed in list.
#len(A)-1 stands for the high index.
def quick_sort(A):
#pass in A, low index, high(ending) index
    quick_sort2(A, 0, len(A)-1)

#If there is a more than one item to be sorted
#I am going to call partition function(where...is it from?)
#and the partition function will returns the pivot.
#Examples of the recursions can be seen here.
def quick_sort2(A, low, hi):


    if low < hi:

#Partition functions will return the pivot.
        p = partition(A, low, hi)

#left of the pivot
        quick_sort2(A, low, p - 1)

#right of the pivot
        quick_sort2(A, p + 1, hi)

#Pass in the list,
#the low index,
#and the high index.
def get_pivot(A, low, hi):
    
#Making the middle index.
#It's just the average of low and the high.
    mid = (hi + low) // 2

#the bottom statement is meaningless.
    pivot = hi

#
#I am trying to find the middle index.
#
#so my sorting is at the best shape.
    if A[low] < A[mid]:

        if A[mid] < A[hi]:

            pivot = mid

    elif A[low] < A[hi]:

        pivot = low

    return pivot


def partition(A, low, hi):

#Really,just the index of the pivot.
    pivotIndex = get_pivot(A, low, hi)

#pivot value for the comparisons.
    pivotValue = A[pivotIndex]

#    A[pivotIndex], A[low] = A[low], A[pivotIndex]

    tmp = A[pivotIndex]

    A[pivotIndex] = A[low]

    A[low] = tmp

    border = low

#iteration begins from low to high value.
    for i in range(low, hi + 1):

#If item is lower than the pivot value.
        if A[i] < pivotValue:

            border += 1
#Then I want to swap it with the pivot value.
#
#
#            A[i], A[border] = A[border], A[i]

            tmp = A[border]

            A[border] = A[i]

            A[i] = tmp


#    A[low], A[border] = A[border], A[low]
    tmp = A[low]

    A[low] = A[border]

    A[border] = tmp

#then I return something Q: what is it?
    return(border)

#For the performance sake, the statements below is

#used to use selection sort if I am soring a really small list.

#def qucik_sort2(A, low, hi):

#    if hi-low < threshold and low < hi:

#        quick_selection(A, low, hi)

#    elif low < hi:

#        p = partition(A, low, hi)

#        quick_sort2(A, low, p - 1)

#        quick_sort2(A,p + 1, hi)

#Nothing is being printed.
#BUT, haven't exactly analyzed things yet.

quick_sort(numbers)

print(numbers)