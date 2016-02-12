import sys
sys.path.append('/home/bilongc/projects/leetcode/utils')
from ListNode import ListNode
from ListGen import ListGen

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Use a fake head pointer
        head = ListNode(0)
        result = head
        carry = 0

        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            result.next = ListNode(sum % 10)
            carry = sum/10
            l1 = l1.next
            l2 = l2.next
            result = result.next

        while l1 is not None:
            sum = l1.val + carry
            result.next = ListNode(sum % 10)
            carry = sum/10
            l1 = l1.next
            result = result.next

        while l2 is not None:
            sum = l2.val + carry
            result.next = ListNode(sum % 10)
            carry = sum/10
            l2 = l2.next
            result = result.next

        if carry != 0:
            result.next = ListNode(carry)

        return head.next

lgen = ListGen()
testList0 = lgen.createList([2,4,3])
testList1 = lgen.createList([5,6,4])

sol = Solution()

sol.addTwoNumbers(testList0, testList1).printList()
sol.addTwoNumbers(lgen.createList([5]), lgen.createList([5])).printList()
sol.addTwoNumbers(lgen.createList([9,1,6]), lgen.createList([0])).printList()
