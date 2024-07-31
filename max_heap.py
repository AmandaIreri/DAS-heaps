#1) Implement a function to find the kth largest element in an unsorted array using a heap

import heapq
def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

#2) Implement the heapify operation for a max heap
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

#3) How would you merge k sorted arrays using a heap? Describe the approach and its time complexity.
import heapq

def merge_k_sorted_arrays(arrays):
    result = []
    min_heap = []

    # Push the first element from each array to the heap
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    # Process the heap
    while min_heap:
        val, array_index, element_index = heapq.heappop(min_heap)
        
        # Add the smallest element to the result
        result.append(val)
        
        # If there are more elements in the array, push the next one
        if element_index + 1 < len(arrays[array_index]):
            next_element = arrays[array_index][element_index + 1]
            heapq.heappush(min_heap, (next_element, array_index, element_index + 1))

    return result

# Example usage
arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
print(merge_k_sorted_arrays(arrays))

#4) How would you efficiently find the median of a stream of integers?

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # Push to max heap and balance
        heapq.heappush(self.small, -num)
        
        # Ensure every element in small is <= every element in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance the heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2

# Example usage
mf = MedianFinder()
stream = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
for num in stream:
    mf.addNum(num)
    print(f"After adding {num}, median is {mf.findMedian()}")

#5)Implement a function to find the k smallest elements in an unsorted array using a heap.

import heapq

def find_k_smallest(arr, k):
    # Create a max heap
    heap = []
    
    for num in arr:
        # If heap size is less than k, add the element
        if len(heap) < k:
            heapq.heappush(heap, -num)  # Use negative for max heap
        # If current number is smaller than the largest in heap, replace it
        elif -num > heap[0]:
            heapq.heapreplace(heap, -num)
    
    # Convert back to positive and return
    return [-x for x in heap]

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(find_k_smallest(arr, k))