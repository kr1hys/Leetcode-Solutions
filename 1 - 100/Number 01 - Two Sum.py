#Number 1 - Two Sum
class Solution(object):
    def twosum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
        return "Theres no solution possible."

print(Solution().twosum([2,7,11,15], 9))
print(Solution().twosum([3,2,4], 6))
print(Solution().twosum([3,3], 6))
