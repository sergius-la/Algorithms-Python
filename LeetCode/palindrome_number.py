"""
Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads 
the same backward as forward.

https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        if str_num != str_num[::-1]:
            return False
        else:
            return True

sol = Solution()
print(sol.isPalindrome(121)) # True
print(sol.isPalindrome(-121)) # False
print(sol.isPalindrome(10)) # False
