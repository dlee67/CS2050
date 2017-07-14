numbers = [1,35,42,53,6,12,4]

#passes in the list
def merge_sort(A):

#low index and high index
    merge_sort2(A, 0, len(A)-1)



def merge_sort2(A, first, last):
    
#if there is more than one item.
#which can be interpreted in the bottom condition.
    if first < last:

        middle = (first + last) // 2

#I perform merge sort on those each halves.
        merge_sort2(A, first, middle)

        merge_sort2(A, middle + 1, last)

#And I combine them together.
        merge(A, first, middle, last)

#
#
#
#
#
def merge(A, first, middle, last):

#left half of my list.
    L = A[first:middle]

#right half of my list.
    R = A[middle:last+1]

#I append really large number so I know that I have reached the end of my list.
    L.append(999999999)

    R.append(999999999)

    i = j = 0

#Someone help me...
#
    for k in range(first, last+1):

        if L[i] <= R[j]:

            A[k] = L[i]

            i += 1

        else:

            A[k] = R[j]

            j += 1

#Nothing is being printed.
#darn
merge_sort(numbers)