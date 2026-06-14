class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node

    def get_pred(self, index: int) -> ListNode:
        """index 바로 앞 노드 반환 (sentinel 포함)"""
        pred = self.head
        for _ in range(index):
            pred = pred.next
        return pred

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self.get_pred(index + 1).val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0

        pred = self.get_pred(index)

        new_node = ListNode(val)
        new_node.next = pred.next
        pred.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        pred = self.get_pred(index)
        pred.next = pred.next.next

        self.size -= 1