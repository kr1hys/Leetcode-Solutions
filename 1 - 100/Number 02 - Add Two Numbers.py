#Number 02 - Add Two Numbers
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(0)
        current=dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            digit = total %10
            carry = total //10

            current.next = ListNode(digit)
            current=current.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        return dummy.next

#the below testing is AI generated (Claude Opus 5.5)   
"""
def build(nums):
    dummy=ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

def show(node):
    out =[]
    while node:
        out.append(node.val)
        node = node.next
    return out

print(show(Solution().addTwoNumbers(build([2,4,3]), build([5,6,4]))))
"""