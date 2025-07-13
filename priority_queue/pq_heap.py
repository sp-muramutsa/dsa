"""
Implementation of a priority queue using a min heap. Ascending order of priority.
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


class PriorityQueue():
    def __init__(self):
        self.heap = []
    
    def parent(self, index: int) -> Optional[int]:
        if index not in range(len(self.heap)):
            return None
        
        return (index - 1) // 2 
        
    
    def left_child(self, index : int) -> Optional[int]:
        left_child_index = (2 * index) + 1
        return left_child_index if left_child_index < len(self.heap) else None

        

    def right_child(self, index : int) -> Optional[int]:
        right_child_index = (2 * index) + 2
        return right_child_index if right_child_index < len(self.heap) else None

    def empty(self) -> bool:
        return not(self.heap)

    def peek(self) -> Optional[Node]:
        if self.empty():
            return None
        return self.heap[0]

    def enqueue(self, node: Node) -> None:
        # Insert at the end
        self.heap.append(node)

        # Heapify up
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, index: int) -> None:
        while index > 0:
            parent_index = self.parent(index)
            if self.heap[parent_index].priority > self.heap[index].priority:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def dequeue(self) -> Optional[Node]:
        if self.empty():
            return None
        
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self.heapify_down(0)
        return root
    
    def heapify_down(self, index: int) -> None:
        while True:
            left_child_index = self.left_child(index)
            right_child_index = self.right_child(index)
            smallest_index = index

            if left_child_index is not None and self.heap[smallest_index].priority > self.heap[left_child_index].priority:
                smallest_index = left_child_index
            
            if right_child_index is not None and self.heap[smallest_index].priority > self.heap[right_child_index].priority:
                smallest_index = right_child_index
            
            if smallest_index != index:
                self.heap[smallest_index], self.heap[index] =  self.heap[index],  self.heap[smallest_index]
                index = smallest_index
            else:
                break

    def traverse(self, index : int) -> None:
        """
        DFS Inorder
        """
        if index is None or index >= len(self.heap):
            return
        
        left_child_index = self.left_child(index)
        right_child_index = self.right_child(index)
        
        self.traverse(left_child_index)

        print(f"[{self.heap[index].value}][{self.heap[index].priority}] -> ", end="")
        self.traverse(right_child_index)
    
    
    def build_priority_queue(self) -> None:
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapify_down(i)
    

    def level_order_traverse(self) -> None:
        print("Level Order Traversal:")
        for node in self.heap:
            print(f"[{node.value}][{node.priority}]", end=" -> ")
        print("None")





a = Node("Raphinha", 1)
b = Node("Pedri", 2)
c = Node("Lamine", 3)
e = Node("Dembouz", 5)
f = Node("Kane", 6)

pq = PriorityQueue()
pq.heap = [b, f, c, a, e]
pq.build_priority_queue()
pq.traverse(0)
print()
pq.enqueue(Node("Salah", 4))
pq.traverse(0)
print()
pq.level_order_traverse()




