# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curNode = head
        # nextNode = head.next
        # if head.next.next == None:
        #     head.next.next = head.next
        #     return
        # if nextNode != None:
        #     reverseList(nextNode)
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

            



        