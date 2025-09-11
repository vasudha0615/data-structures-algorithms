class ListNode:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index):
        if index < 0 or index > self.size:
            return -1

        cur = self.head
        
        while index!=0:
            cur = cur.next
            index-=1

        return cur.value

    def addathead(self,value):
        new_node = ListNode(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size+=1

    def addattail(self,value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size+=1
            

    def addatindex(self,index):
        if index < 0 and index > self.size:
            return -1

        elif index == 0:
            addathead(value)

        elif index == self.size :
            addattail(value)

        else:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
                
            new_node = ListNode(value)

            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
            new_node.prev = cur

            self.size+=1

    def deleteatindex(self,index):
        if index < 0 or index >= self.size :
            return -1
        elif index == 0:
            self.head == self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        elif index == self.size-1:
            self.tail == self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
                cur.prev.next = cur.next
                cur.next.prev = cur.prev

                self.size-=1

obj = LinkedList()
obj.addathead(10)
obj.addattail(15)
obj.addattail(20)
obj.deleteatindex(0)
obj.addathead(40)
 
print(obj.get(1))

        


