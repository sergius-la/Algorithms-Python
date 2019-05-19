class Solution:
    def mergeTwoLists(l1, l2):
        res = [0] * (len(l1) + len(l2))
        i = j = k = 0
        while j < len(l1) - 1 or k < len(l2) - 1:
            if l1[j] <= l2[k]:
                res[i] = l1[j]
                i += 1
                j += 1
            else:
                res[i] = l2[k]
                i += 1
                k += 1
        
        while j != len(l1):
            res[i] = l1[j]
            i += 1
            j += 1
        
        while k !=len(l2):
            res[i] = l2[k]
            i += 1
            k += 1
        
        return res
    

print(Solution.mergeTwoLists([1, 2, 4], [1, 3, 5])) # [1, 1, 2, 3, 4, 5]

