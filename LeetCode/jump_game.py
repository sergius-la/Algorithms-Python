"""
Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""
class Solution:
    def canJump(self, nums) -> bool:
        return False

sol = Solution()
print(sol.canJump([2,3,1,1,4])) # True
print(sol.canJump([3,2,1,0,4])) # False
print(sol.canJump([0])) # True
print(sol.canJump([2, 0])) # True
print(sol.canJump([2,5,0,0])) # True