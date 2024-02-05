from typing import Optional
        

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Removes the nth node from the end of a singly-linked list.
    Parameters:
    - head ('ListNode'): The head of the linked list.
    - n (int): The position of the node to be removed from the end.
    Returns:
    - 'ListNode': The head of the modified linked list.
    """
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    count = count - n
    current = head
    if count == 0 and current:
        current = current.next
        return current
    i = 1
    while i < count:
        current = current.next
        i += 1
    if current.next:
        current.next = current.next.next
    return head