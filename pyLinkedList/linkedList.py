class Node:
    """
    Node in Linked List
    """

    def __init__(self, head, next=None):
        self.head = head
        self.next = next


def initLinkedList(elements):
    """
    Initialize linked list with elements
    """
    
    if not elements:
        return None

    head = Node(elements[0])
    current = head

    for element in elements[1:]:
        current.next = Node(element)
        current = current.next

    return head


def hasCycle(head):
    """
    Check if the linked list has a cycle using Floyd's Tortoise and Hare algorithm.
    """
    
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False
