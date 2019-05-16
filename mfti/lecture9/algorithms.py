def mergeSort(a):
    if len(a) <= 1:
        return 

    middle = len(a) // 2
    l = [a for i in range(0, middle)]
    r = [a for i in range(middle, len(a))]
    mergeSort(l)
    mergeSort(r)
    res = merge(l, r)
    for i in range(len(res)):
        a[i] = res[i]


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
    

# Сортировка Тони Хора QuickSort

def tony(a):
    if len(a) <= 1:
        return
    bar = a[0]
    l = []
    m = []
    r = []
    for x in a:
        if x < bar:
            l.append(x)
        elif x == bar:
            m.append(x)
        else:
            r.append(x)
    tony(l)
    tony(r)
    k = 0
    for x in l + m + r:
        a[k] = x
        k += 1

def check_sorted(a, assending=True):
    flag = True
    s = 2 * int(assending) - 1
    for i in range(0, len(a)-1):
        if s * a[i] > s * a[i+1]:
            flag = False
            break
    return flag