# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 22:34:52 2021

@author: tyu6
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head is None:
            return head

        head.next = self.removeElements(head.next, val)
        if head.val == val:
            next_node = head.next
        else:
            next_node = head
        return next_node