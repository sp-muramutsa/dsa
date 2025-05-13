class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def __str__(self):
        return str(self.heap)
    
    def _parent(self, index):
        if index <= 0:
            return None
        return (index - 1) // 2
    
    def _left_child(self, index):
        left_child_index = 2 * index + 1
        if left_child_index >= len(self.heap):
            return None
        return left_child_index

    def _right_child(self, index):
        right_child_index = 2 * index + 2 
        if right_child_index >= len(self.heap):
            return None
        return right_child_index 
    
    def _heapify_up(self, index):
        while index > 0:
            parent_index = self._parent(index)

            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    

    def _heapify_down(self, index):
        largest = index
        left_child_index = self._left_child(index)
        right_child_index = self._right_child(index)

        if left_child_index is not None and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        
        if right_child_index is not None and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
    
    def _extract_max(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._heapify_down(0)
        return root
    
    def _delete(self, index):
        if index >= len(self.heap) or index < 0:
            return False
        
        self.heap[index] = self.heap[-1]
        self.heap.pop()
               
   
        parent_index = self._parent(index)

        if parent_index and self.heap[index] > self.heap[parent_index]:
            self._heapify_up(index)
        else:
            self._heapify_down(index)
        
        return True

def build_max_heap( arr):
    max_heap = MaxHeap()
    max_heap.heap = arr
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heap._heapify_down(i)
    
    return max_heap


arr = [50, 70, 90, 20, 21, 34, 56, 7, 1, -1, -2]
max_heap = build_max_heap(arr)
print(max_heap)
