class ListNode():
    def __init__(self, val:int, next=None):
        self.val = val
        self.next = next
    
    def print_list_node(self):
        if self != None:
            print(self.val)
        if self.next != None:
            self.next.print_list_node()
    
    # My solution: a bit more convoluted
    def reverse_list_node(self):
        # list is not empty
        if self != None:
            prev = None
            curr = self
            while curr.next != None:
                # reverse
                nxt = curr.next
                curr.next = prev
                # update
                prev = curr
                curr = nxt
            curr.next = prev
            return curr
    # Neetcode solution: less convoluted in that it needs only check `curr`
    def reverseList(self):
        prev = None
        curr = self
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
        

values = [1, 5, 7, 12]
a = ListNode(values[0])
b = ListNode(values[1])
c = ListNode(values[2])
d = ListNode(values[3])
a.next = b
b.next = c
c.next = d

a.print_list_node()
print()
last = a.reverseList()
last.print_list_node()



