#Number 26 - Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[k]=nums[i]
                k+=1
        return k

print(Solution().removeDuplicates([1,1,2]))