from typing import List
import heapq


def k_merge(lists: List[list]) -> List:
    """
    Merges k sorted lists and returns one sorted list

    Uses a min heap of (number, list_index, number_index)
    """

    min_heap = []
    n = len(lists)

    # Insert first element
    for i in range(n):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))
    
    # Merge the arrays
    sorted_list = []
    while min_heap:
        
        number, list_index, number_index = heapq.heappop(min_heap)
        
        if number_index + 1 < len(lists[list_index]):
            heapq.heappush(min_heap, (lists[list_index][number_index + 1], list_index, number_index + 1))
        
        sorted_list.append(number)
    
    return sorted_list

            



lists = [[1, 4, 5], [1, 3, 4],[2, 6]]
print(k_merge(lists))
# Expected output: [1, 1, 2, 3, 4, 4, 5, 6]


lists = [[0, 8, 10], [2], [1, 3, 3, 4, 5],[]]
print(k_merge(lists))
# Expected output: [0, 1, 2, 3, 3, 4, 5, 8, 10]

lists = [[-10, -5, -1],[-6, -4, -2],[-5, -3, -3, -1]]
print(k_merge(lists))
# Expected output: [-10, -6, -5, -5, -4, -3, -3, -2, -1, -1]

