class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data, end=' ')
            current = current.prev
        print()

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current.next is None:
                    current.prev.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            current.next, current.prev = current.prev, current.next
            prev_node = current
            current = current.prev

        if prev_node:
            self.head = prev_node



ll = DoublyLinkedList()

ll.append(2)
ll.prepend(3)
ll.reverse()
ll.display_backward()