class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    slow = head
    fast = head
    
    # While fast hasn't reached the end or the last node
    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
    # When fast hits the end, slow is at the middle
    return slow

# Helper to create a list for testing: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

middle = find_middle(head)
print(f"The middle node value is: {middle.val}")

# here i am going to test whether the ai review is generating or not 
