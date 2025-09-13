class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(f" <- [{curr.data}] -> ", end="")
            curr = curr.next
        print()

    def insert_at_beginning(self, value):
        new_node = Node(value)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            return self.insert_at_beginning(value)

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    def insert_at_position(self, value, position):
        new_node = Node(value)
        if not self.head or position == 0:
            return self.insert_at_beginning(value)

        curr = self.head

        for i in range(position - 1):
            curr = curr.next

        node_at_prev = curr.prev
        node_at_prev.next = new_node
        new_node.prev = node_at_prev

        curr.prev = new_node
        new_node.next = curr

    def delete_at_beginning(self):
        old_head = self.head
        new_head = old_head.next
        self.head = new_head
        old_head = None

    def delete_at_end(self):
        curr = self.head

        while curr.next is not None:
            curr = curr.next
        print(curr.data)

        old_tail = curr
        new_tail = old_tail.prev
        new_tail.next = None
        old_tail.data = None

    def delete_at_position(self, position):
        if not self.head or position == 0:
            return

        curr = self.head
        for i in range(position - 1):
            curr = curr.next

        nxt = curr.next
        prev = curr.prev
        prev.next = nxt
        nxt.prev = prev
        curr.data = None

    def search(self, target):
        curr = self.head

        while curr is not None:
            if curr.data == target:
                return True
            curr = curr.next
        return False

    def bubble_sort(self):
        curr = self.head

        while curr is not None:
            iterator = curr.next
            while iterator is not None:
                if curr.data > iterator.data:
                    curr.data, iterator.data = iterator.data, curr.data
                iterator = iterator.next
            curr = curr.next


dll = DLL()
dll.insert_at_beginning(10)
dll.insert_at_end(30)

dll.insert_at_end(70)
dll.insert_at_end(80)
dll.insert_at_end(20)
dll.insert_at_end(50)
dll.insert_at_end(40)
dll.insert_at_end(60)

dll.print_list()
print(dll.bubble_sort())
dll.print_list()
