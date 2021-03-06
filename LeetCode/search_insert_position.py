"""
Search Insert Position

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l = -1
        r = len(nums)
        while r - l > 1:
            middle = (r + l) // 2
            if nums[middle] < target:
                l = middle
            else:
                r = middle
        return l + 1

sol = Solution()
print(sol.searchInsert([1,3,5,6], 5)) # 2
print(sol.searchInsert([1,3,5,6], 2)) # 1
print(sol.searchInsert([1,3,5,6], 7)) # 4
print(sol.searchInsert([1,3,5,6], 0)) # 0