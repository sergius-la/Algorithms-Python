"""
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.

https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    def reverse(self, x: int) -> int:
        sing = -1 if x < 0 else 1
        num = 0
        check = abs(x)
        while check > 0:
            num *= 10
            num += check % 10
            check = check // 10
        if(abs(num) > (2 ** 31 - 1)):
            return 0 
        return num * sing

sol = Solution()
print(sol.reverse(123)) # 321
print(sol.reverse(-123)) # -321
print(sol.reverse(120)) # 21
print(sol.reverse(1_534_236_469)) # 0