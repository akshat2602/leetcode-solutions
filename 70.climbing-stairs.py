#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        prev_prev = 1
        prev = 2
        curr = 0

        for _ in range(3, n + 1):
            temp = prev_prev + prev
            curr = temp
            prev_prev = prev
            prev = curr

        return curr


# @lc code=end
