#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.63%)
# Likes:    3101
# Dislikes: 4897
# Total Accepted:    1M
# Total Submissions: 4M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 :
            return 0
        
        if (x < 0) :
            neg = True
        else :
            neg = False

        numStr = str(abs(x))
        numStr = numStr[::-1]
        if (neg == True) :
            result = int('-' + numStr)
        else :
            result = int(numStr)

        max_result = pow(2,31)
        if ( -max_result < result < max_result - 1) :
            return result
        else :
            return 0


# @lc code=end

