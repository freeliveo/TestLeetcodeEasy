#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        f,s = 1,1
        while f<n:
            if nums[f]!=nums[s-1]:
                nums[s]=nums[f]
                s+=1
            f+=1
        return s

# @lc code=end