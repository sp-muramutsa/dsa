"""
Implementation of a min heap. This is a complete binary tree in which 
each node is less than its children.
    0-indexed
    1. parent(): child at i, parent at (i-1) // 2
    2. left_child(): parent at i, left child at 2(i+1)
    3. right_child(): parent at i, right child at 2(i+1)

    4. insert(node): insert at the end of list, heapify up
    5. heapify_up(node): while the list is in bounds on the left(we haven't reached the top of the tree):
        - find the parent index 
        - if the parent is less than the node
            - swap them
            - update the index to the parent index bc that's where node is at right now
    6. heapify_down(node): find the smallest among left and right child, exchange them and keep moving down the tree.

    We always replace whatever we are deleting with the last node to keep the complete binary tree property i.e. everything filled left to right
    7. extract_min(node): delete the min(topmost), bring in the last node and heapify down.
    8. delete(node): replace it with the last element. If it's parent is bigger, heapify up. Else, heapify down.

    9. build_min_heap(list): Get a range of all parents and heapify each of them down.
"""


class MinHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def _parent(self, index):
        if index == 0:
            return None
        return (index - 1) // 2

    def _left_child(self, index):
        left_child_index = 2 * index + 1

        if left_child_index >= len(self.heap):
            return None
        return left_child_index

    def _right_child(self, index):
        right_child_index = (2 * index) + 2

        if right_child_index >= len(self.heap):
            return None
        return right_child_index

    def _insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = self._parent(index)
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index],
                )
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest = index

            if left is not None and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right is not None and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[smallest], self.heap[index] = (
                    self.heap[index],
                    self.heap[smallest],
                )
                index = smallest
            else:
                break

    def _extract_min(self):
        if not self.heap:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._heapify_down(0)
        return root

    def _delete(self, index):
        if index >= len(self.heap):
            return

        self.heap[index] = self.heap[-1]
        self.heap.pop()

        parent = self._parent(index)

        if index > 0 and self.heap[index] < self.heap[parent]:
            self._heapify_up(index)
        else:
            self._heapify_down(index)

        return True

    def build_min_heap(self, arr):
        self.heap = arr
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            min_heap._heapify_down(i)

        return self


min_heap = MinHeap()
# min_heap.heap = [10, 20, 30, 40, 50, 60, 70]
# min_heap._delete(2)
arr = [40, 20, 30, 10, 50, 60, 70]
min_heap.build_min_heap(arr)
print(min_heap)
