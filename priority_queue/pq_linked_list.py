"""
Implementation of a priority queue using a linked list. Ascending order of priority.
1. empty(): O(1)
2. peek(): O(1)
3. enqueue(node): O(n)
4. dequeue(): O(1)
5. traverse()
"""

from typing import Optional


class Node():

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None


class PriorityQueue():
    def __init__(self):
        self.front = None

    def empty(self) -> bool:
        return self.front is None

    def peek(self) -> Optional[Node]:
        return self.front

    def enqueue(self, node: Node) -> None:
        
        if self.empty():
            self.front = node
            return

        if self.front.priority > node.priority:
            node.next = self.front
            self.front = node

        else:
            curr = self.front
            while curr.next and curr.next.priority <= node.priority:
                curr = curr.next
            
            temp = curr.next
            curr.next = node
            node.next = temp      


    def dequeue(self) -> Optional[Node]:
        
        if self.empty():
            raise Exception("can't dequeue from an empty priority queue")
        
        temp = self.front
        self.front = self.front.next
        return temp

    def traverse(self) -> None:
        curr = self.front

        while curr:
            print(f"[{curr.value}][{curr.priority}] -> ", end="")
            curr = curr.next
        print()


a = Node("Raphinha", 1)
b = Node("Pedri", 2)
c = Node("Lamine", 3)
e = Node("Dembouz", 5)
f = Node("Kane", 6)

pq = PriorityQueue()
pq.enqueue(a)
pq.enqueue(b)
pq.enqueue(c)
pq.enqueue(e)
pq.enqueue(f)

pq.traverse()

pq.enqueue(Node("Salah", 4))

pq.traverse()

  

