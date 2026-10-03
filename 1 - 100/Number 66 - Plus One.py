#Number 66 - Plus One
class Solution(object):
    def plusOne(self, digits):
        final = len(digits) -1
        while final>=0 and digits[final] == 9:
            digits[final] = 0
            final -= 1
        if final < 0:
            digits.insert(0,1)
        else:
            digits[final] += 1
        return digits 

print(Solution().plusOne([4,3,2,1]))
print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([9]))