#Number 20 - Valid Parentheses
class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {"[":"]","{":"}","(":")"}
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack or pairs[stack.pop()] != i:
                    return False
        return not stack
        
print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('(]'))
print(Solution().isValid('([])'))
print(Solution().isValid('([)]'))
