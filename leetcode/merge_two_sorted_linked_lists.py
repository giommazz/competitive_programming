class ListNode:
    """Singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def argmin_listnode_with_other(node1, node2, key=lambda x: x.val):
    """Return a tuple (main, supp) where main is the node with the smaller key value and supp is the other."""
    if key(node1) <= key(node2):
        return node1, node2
    else:
        return node2, node1

# Time complexity O(m+n), space complexity O(1).
def mergeTwoLists(l1, l2):
    """In-place merge two sorted linked lists l1 and l2 into a single sorted list and return the head."""
    if not l1: # if only `l2` exists
        return l2
    if not l2: # if only `l1` exists
            return l1
    # if both exist
    main, supp = argmin_listnode_with_other(l1, l2) # `main` becomes list with smaller head
    head = main # `head` is the pointer to the final list
    while main and supp:
        # always compare 3 elements: `main`, `main.next`, `supp`
        nxt = main.next
        if nxt: # if `nxt` is not None (end of list)
            if nxt.val <= supp.val: # just advance on current `main`-list
                main = main.next
            else:
                main.next = supp # link `main`-list to `supp`-list
                supp = nxt # `supp` becomes `main.next`
                main = main.next # move `main`
        else: # you reached the end of `main`
            main.next = supp # just link `main` to `supp`, which is already sorted
            break
    return head

# Alternative solution: time complexity O(m+n), space complexity O(1).
def mergeTwoLists_dummy(l1, l2):
    """Iterative merge using a dummy node. O(m+n) time, O(1) extra space."""
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    # append remaining unmerged part of the list to the merged list in one step
    tail.next = l1 or l2 # assign `tail.next` to whichever of `l1` or `l2` is not None. 
    return dummy.next
        
        