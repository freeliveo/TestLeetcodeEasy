#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        y = x[::-1]
        if "".join(x) == "".join(y):
            return True
        else:
            return False
# @lc code=end

