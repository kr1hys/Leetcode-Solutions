#Number 14 - Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        common = ""
        characterend = 0
        smallest=strs.index(min(strs, key=len))
        for i in range(len(strs[smallest])):
            for j in range(len(strs)):
                if strs[j][i] != strs[smallest][i]:
                    characterend = i
                    for k in range(characterend):
                        common+=strs[smallest][k]
                    return common
        return strs[smallest]
    
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
