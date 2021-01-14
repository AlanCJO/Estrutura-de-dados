def minorSearch(arr):
    smaller = arr[0]
    lowest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            lowest_index = i 
    return lowest_index

def ordination(arr):
    array = arr.copy()
    newArray = list()
    for _ in range(len(array)):
        index = minorSearch(array)
        newArray.append(array.pop(index))
    return newArray
