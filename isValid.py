#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        if s == '':
            return True
        else:
            return False
# @lc code=end

