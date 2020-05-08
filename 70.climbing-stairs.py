#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (46.39%)
# Likes:    3824
# Dislikes: 125
# Total Accepted:    629.8K
# Total Submissions: 1.4M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#

# @lc code=start
class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        else :
            return self._climbStairs(n-1) + self._climbStairs(n-2)
    
    def _climbStairs(self, n: int):
        if n not in self.cache.keys() :
            self.cache[n] = self.climbStairs(n)
        return self.cache[n]

# @lc code=end

