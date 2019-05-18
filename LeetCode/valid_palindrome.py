class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        left = ""
        rigth = ""
        while i < len(s) / 2:
            while not s[i].isalnum() and i < len(s) - 1:
                i += 1
            left = s[i].lower() if s[i].isalnum() else "" 
            
            while not s[j].isalnum() and j > 0:
                j -= 1
            rigth = s[j].lower() if s[j].isalnum() else ""

            if left == rigth:
                i += 1
                j -= 1
            else:
                return False
        return True


sol = Solution()
assert sol.isPalindrome("A man, a plan, a canal: Panama") # True
assert not sol.isPalindrome("race a car") # False
assert sol.isPalindrome(" ") # True
assert sol.isPalindrome(".,") # True