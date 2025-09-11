class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

class solution:
    def reverselist(self,head):
        pre = None
        cur = head
        suc = None

        while cur:
            suc = cur.next
            cur.next = pre
            pre = cur
            cur = suc

        return pre
