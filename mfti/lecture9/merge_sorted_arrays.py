"""
Merge Sorted Arrays
"""

def merge(a, b):
    res_len = len(a) + len(b)
    res = [0] * res_len
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            res[n] = a[i]
            i += 1
            n += 1
        else:
            res[n] = b[k]
            k += 1
            n += 1
    
    while i < len(a):
        res[n] = a[i]
        i += 1
        n += 1

    while k < len(b):
        res[n] = b[k]
        n += 1
        k += 1
    return res

a = [1, 2, 3]
b = [1, 2, 3]

print(merge(a, b)) # [1, 1, 2, 2, 3, 3]