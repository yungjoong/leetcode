#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (51.83%)
# Likes:    3747
# Dislikes: 550
# Total Accepted:    927.6K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None :
            return l2
        
        if l2 is None :
            return l1
        
        if (l1.val > l2.val) :
            head = ListNode(l2.val)
            head.next = self.mergeTwoLists(l1, l2.next)
        else :
            head = ListNode(l1.val)
            head.next = self.mergeTwoLists(l1.next, l2)
            
        return head
        
# @lc code=end

