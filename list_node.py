# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"

    def reverseList(self):
        # node that has already been processed, initialized to None
        prev = None
        # node that is being processed right now
        curr = self
        while curr:
            # node after `curr`, that must be saved before overriding `curr.next`
            nxt = curr.next
            # reverse
            curr.next = prev
            # advance `prev`
            prev = curr
            # advance `curr`
            curr = nxt
        
        return prev

    def get_list(self):
        if self.next is None:
            return [self.val]
        else:
            return [self.val] + self.next.get_list()

n0 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n0.next = n1
n1.next = n2
n2.next = n3

print(f"original list: {n0.get_list()}")
new_pointer = n0.reverseList()
print(f"new pointer is {new_pointer.val} -> {new_pointer.next}")
print(new_pointer.get_list())