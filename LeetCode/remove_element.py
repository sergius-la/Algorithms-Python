class Solution:
    def removeElement(self, nums, val: int) -> int:
        nums_len = len(nums)
        if nums_len == 0: return 0
        i = j = 0
        temp = 0
        while i < nums_len:
            if nums[i] == val:
                j = i + 1
                while j < nums_len:
                    if nums[j] != val:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        i -= 1
                        break
                    j += 1
            i += 1
        res = nums_len
        for x in nums[::-1]:
            if x == val:
                res -= 1
            else:
                break
        return res

sol = Solution()
print(sol.removeElement([3,2,2,3], 3)) # 2
print(sol.removeElement([0,1,2,2,3,0,4,2], 2)) # 5