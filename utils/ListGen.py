from ListNode import ListNode
from collections import deque

class ListGen:
    def __init__(self):
        return

    def createList(self, arr):
        head = ListNode(0)
        iter = head

        for elem in arr:
            iter.next = ListNode(elem)
            iter = iter.next

        return head.next
