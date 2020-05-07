#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.47%)
# Likes:    582
# Dislikes: 2252
# Total Accepted:    356.3K
# Total Submissions: 1.1M
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word (last word means the last
# appearing word if we loop from left to right) in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a maximal substring consisting of non-space
# characters only.
# 
# Example:
# 
# 
# Input: "Hello World"
# Output: 5
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        prv = 0
        for ch in s :
            if ch == ' ' :
                if cnt != 0 :
                    prv = cnt
                cnt = 0                
            else :
                cnt += 1
        if cnt == 0 :
            return prv
        else :
            return cnt
# @lc code=end

