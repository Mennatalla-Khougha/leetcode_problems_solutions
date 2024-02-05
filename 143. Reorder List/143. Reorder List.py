from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def reorderList(self, head: Optional[ListNode]) -> None:
    """Reorder a linked list to be is the following order L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

    Args:
        head (Optional[ListNode]): The head of a linked list
    """

    slow, fast = head, head.next
    
    # Determine where the second half of the list begin using fast and slow pointers
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    prev = slow.next = None

    # Reverse the second half of the list
    while second:
        next = second.next
        second.next = prev
        prev = second
        second = next
    second, first = prev, head

    # Merge the 2 lists
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        second, first = temp2, temp1
