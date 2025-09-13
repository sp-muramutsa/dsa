class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Singly-linked Linked List
class SLL:
    def __init__(self):
        self.head = None

    def printSLL(self):
        val = self.head
        while val is not None:
            print(val.data, end=" -> ")
            val = val.next

        print("\n")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def insert_at_position(self, position, data):
        if position == 0:
            return self.insert_at_beginning(data)

        new_node = Node(data)
        temp = self.head
        for i in range(position - 1):
            # Only added the if-else clause to be able to add at the end. In case you are not worried about going out of bounds, "temp = temp.next" suffices.
            if temp.next:
                temp = temp.next
            else:
                break

        node_at_pos = temp.next
        temp.next = new_node
        new_node.next = node_at_pos

    def delete_at_beginning(self):
        self.head = self.head.next

    def delete_at_end(self):
        curr_node = self.head
        while curr_node.next.next is not None:
            curr_node = curr_node.next
        curr_node.next = None

    def delete_at_position(self, position):
        if position == 0:
            return self.delete_at_beginning()

        curr_node = self.head
        for i in range(position - 1):
            curr_node = curr_node.next

        prev = curr_node
        node_at_position = prev.next
        next_node = node_at_position.next

        node_at_position = None
        prev.next = next_node

    def search(self, target):
        temp = self.head
        while temp.data is not None:
            if temp.data == target:
                return True
            temp = temp.next
        return False

    # Bubble sort
    def sort(self):
        if self.head is None:
            return

        curr = self.head
        while curr is not None:
            iterator = curr.next

            while iterator is not None:
                if curr.data > iterator.data:
                    curr.data, iterator.data = iterator.data, curr.data

                iterator = iterator.next
            curr = curr.next


l1 = SLL()
l1.head = Node(50)
e2 = Node(60)
e3 = Node(30)

l1.head.next = e2
e2.next = e3

l1.insert_at_beginning(90)
l1.insert_at_beginning(40)
l1.insert_at_beginning(70)
l1.insert_at_beginning(90)
l1.insert_at_end(20)
l1.insert_at_position(50, 60)
# # l1.delete_at_beginning()
# l1.delete_at_end()
# l1.delete_at_position()
l1.printSLL()
l1.printSLL()
