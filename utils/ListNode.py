# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        iter = self
        result = ""

        while iter is not None:
            result = result + str(iter.val) + "->"
            iter = iter.next

        print result
