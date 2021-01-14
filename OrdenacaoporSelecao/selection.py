def minorSearch(arr):
    smaller = arr[0]
    lowest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            lowest_index = i 

def ordination(arr):
    