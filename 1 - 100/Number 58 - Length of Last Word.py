#Number 58 - Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        #return len(s.split()[-1])
        length = 0
        i = len(s) - 1
        while i>=0 and s[i]==" ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1 
            i -= 1
        return length
    
print(Solution().lengthOfLastWord("Hello World"))