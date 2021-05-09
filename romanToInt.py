#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000}
        sum = 0
        for i in range(len(s)-1):
            if dict[s[i]]<dict[s[i+1]]:
                sum-=dict[s[i]]
            else:
                sum+=dict[s[i]]
        sum+=dict[s[-1]]
        return sum 
# @lc code=end

