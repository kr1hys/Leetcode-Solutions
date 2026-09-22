#Number 13 - Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        romanint = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0 
        #flip it round
        #add every number together unless its a smaller value from the dic after a bigger number
        for i in range(len(s)):
            if i+1 == len(s):
                total += romanint[s[i]]
            elif romanint[s[i]] < romanint[s[i+1]]:
                total -= romanint[s[i]]
            else:
                total += romanint[s[i]]
        return total
    
print(Solution().romanToInt('III'))
print(Solution().romanToInt('LVIII'))
print(Solution().romanToInt('MCMXCIV'))