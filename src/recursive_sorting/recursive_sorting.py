# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    firstArr = 0
    secondArr = 0
    for i in range( 0, elements ):
        if firstArr >= len(arrA):    
            merged_arr[i] = arrB[secondArr]
            secondArr += 1
        elif secondArr >= len(arrB):  
            merged_arr[i] = arrA[firstArr]
            firstArr += 1
        elif arrA[firstArr] < arrB[secondArr]:  
            merged_arr[i] = arrA[firstArr]
            firstArr += 1
        else:  
            merged_arr[i] = arrB[secondArr]
            secondArr += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1 :
        return arr
    left = arr[0: len(arr) // 2]
    right = arr[len(arr) // 2: len(arr)]
    sortedLeft = merge_sort(left)
    sortedRight = merge_sort(right)
    arr = merge(sortedLeft, sortedRight)   
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
