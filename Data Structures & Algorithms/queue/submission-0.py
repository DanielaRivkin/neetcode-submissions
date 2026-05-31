class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Deque:
    def __init__(self):
        self.left = self.right = None

    def isEmpty(self) -> bool:
        return self.left is None

    def append(self, value: int) -> None:
        newNode = ListNode(value)

        # Queue is non-empty
        if self.right:
            self.right.next = newNode
            self.right = newNode
        # Queue is empty
        else:
            self.left = self.right = newNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)

        if self.left:
            newNode.next = self.left
            self.left = newNode
        else:
            self.left = self.right = newNode

    def pop(self) -> int:
        # Queue is empty
        if not self.right:
            return -1  # Explicitly return -1 when empty

        # Special case: Only one element
        if self.left == self.right:
            val = self.right.val
            self.left = self.right = None
            return val

        # Traverse to the second-to-last node
        current = self.left
        while current.next != self.right:
            current = current.next

        # Remove the last node
        val = self.right.val
        self.right = current
        self.right.next = None
        return val

    def popleft(self) -> int:
        # Queue is empty
        if not self.left:
            return -1  # Explicitly return -1 when empty

        # Remove left node and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left:  # If the queue becomes empty
            self.right = None
        return val
