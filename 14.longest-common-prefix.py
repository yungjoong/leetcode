#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.83%)
# Likes:    2278
# Dislikes: 1758
# Total Accepted:    697.8K
# Total Submissions: 2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        if not strs :
            return ret
        minStr = min(strs, key=len)
        for i in range(len(minStr)) :
            cur = strs[0][i]
            for j in range(1, len(strs)) :
                if strs[j][i] != cur :
                    return ret
            ret = ret + cur
        
        return ( ret )          

# @lc code=end

