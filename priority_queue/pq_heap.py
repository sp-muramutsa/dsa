"""
Implementation of a priority queue using a linked list. Ascending order of priority.
1. empty(): O(1)
2. peek(): O(1)
3. enqueue(node): O(logn)
4. dequeue(): O(logn)
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
        pass

    def peek(self) -> Optional[Node]:
        pass

    def enqueue(self, node: Node) -> None:
        pass

    def dequeue(self) -> Optional[Node]:
        pass

    def traverse(self) -> None:
        pass


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

  

