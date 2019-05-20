"""
Binary Search in the sorted array
"""

a = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]

def left_bound(A, key):
    left = -1
    rigth = len(A)
    while rigth - left > 1:
        middle = (left + rigth) // 2
        if A[middle] < key:
            left = middle
        else:
            rigth = middle
    return left

def rigth_bound(A, key):
    left = -1
    rigth = len(A)
    while rigth - left > 1:
        middle = (left + rigth) // 2
        if A[middle] <= key:
            left = middle
        else:
            rigth = middle
    return rigth

def binary_search(A, key):
    left = left_bound(A, key)
    rigth = rigth_bound(A, key)
    if rigth - left > 1:
        return True
    else:
        return False

print(binary_search(a, 1)) # True
print(binary_search(a, -1)) # False
print(binary_search(a, 11)) # False

