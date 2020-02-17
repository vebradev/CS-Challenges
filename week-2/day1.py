# Binary search

numbers = [1, 3, 4, 7, 8, 11, 12, 14, 25]

def binary_search(n, l = numbers):
    start = 0
    end = len(l) - 1
    
    while start <= end:
        middle = (start + end) / 2
        if n < l[middle]:
            end = middle - 1
        elif n > l[middle]:
            start = middle + 1
        else:
            return middle
    return -1
    
binary_search(12)