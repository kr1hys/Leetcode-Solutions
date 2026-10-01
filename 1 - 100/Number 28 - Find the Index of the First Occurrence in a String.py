#Number 28 - Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            count = 0
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    count+=1
                    if count == len(needle):
                        return i
                else: 
                    break
        return -1

print(Solution().strStr("sadbutsad","sad"))   
print(Solution().strStr("leetcode","leeto"))            