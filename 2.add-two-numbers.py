#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.02%)
# Likes:    7749
# Dislikes: 1988
# Total Accepted:    1.3M
# Total Submissions: 4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 == None and l2 == None :
            return None

        if l1 == None :
            l1 = ListNode(0)
    
        if l2 == None :
            l2 = ListNode(0)

        val = (l1.val + l2.val) % 10
        head = ListNode(val)

        if l1.val + l2.val >= 10 :
            if l1.next == None :
                l1.next = ListNode(1)
            else :
                l1.next.val += 1

        head.next = self.addTwoNumbers(l1.next, l2.next)

        return head

# @lc code=end

