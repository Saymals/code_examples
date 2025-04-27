class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return ' -> '.join(str(x) for x in self) + ' -> None'

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=' -> ')
            current = current.next
        print(None)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

    def appstart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self, data=None):
        if self.head is None:
            print('Empty')
            return

        current = self.head

        if current.data == data:
            self.head = current.next
            return

        prev = None
        while current and (current.data != data if not data is None else not current.next is None):
            prev = current
            current = current.next

        if current is None or (data is not None and current.data != data):
            print('Element not found')
            return
        if prev is None:
            self.head = None
            return
        prev.next = current.next

    def popleft(self):
        if self.head is None:
            print('Empty')
            return

        self.head = self.head.next

    def search(self, data):
        current = self.head

        while current.next and current.data != data:
            current = current.next

        return current.data == data

    def reverse(self):
        current = self.head
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev





ll = LinkedList()
for i in ll:
    print(i)

