#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.24%)
# Likes:    4571
# Dislikes: 207
# Total Accepted:    936.3K
# Total Submissions: 2.4M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for ch in s :
            if ch == '(' or ch == '{' or ch == '[' :
                l.append(ch)
            else :
                if len(l) == 0 :
                    return False
                elif ch == ')' :
                    if l.pop() != '(' :
                        return False
                elif ch == '}' :
                    if l.pop() != '{' :
                        return False
                elif ch == ']' :
                    if l.pop() != '[' :
                        return False

        return len(l) == 0
# @lc code=end

