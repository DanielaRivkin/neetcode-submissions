
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next  # Skip the dummy node
        for i in range(index):
            if not curr:
                return -1  # Return -1 for out-of-bounds index
            curr = curr.next
        return curr.val if curr else -1

        

    def insertHead(self, val: int) -> None:
        toInsert = ListNode(val)
        toInsert.next = self.head.next
        self.head.next = toInsert
        if self.tail == self.head:  # If the list was empty
            self.tail = toInsert

        

    def insertTail(self, val: int) -> None:
        toInsert = ListNode(val)
        self.tail.next = toInsert
        self.tail = toInsert

    def remove(self, index: int) -> bool:
        curr = self.head  # Start from dummy node
        for i in range(index):
            if not curr.next:  # Out of bounds
                return False
            curr = curr.next
    
        if curr.next:  # Node to remove exists
            if curr.next == self.tail:  # Update tail if needed
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

        
    def getValues(self) -> List[int]:
        curr = self.head.next  # Skip the dummy node
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


        
