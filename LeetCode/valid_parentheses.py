class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        check = []
        c = ""
        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{": 
                check.append(s[i])
            if s[i] == ")" and len(check) > 0:
                c = check.pop()
                if c != "(": return False
            if s[i] == "]" and len(check) > 0:
                c = check.pop()
                if c != "[": return False
            if s[i] == "}" and len(check) > 0:
                c = check.pop()
                if c != "{": return False
        if len(check) == 0:
            return True
        elif len(check) > 0: 
            return False

sol = Solution()
assert sol.isValid("()") # True
assert sol.isValid("()[]{}") # True
assert not sol.isValid("(]") # False
assert not sol.isValid("([)]") # False
assert sol.isValid("{[]}") # True
assert sol.isValid("") # True
assert not sol.isValid("]") # False
assert not sol.isValid("){") # False


