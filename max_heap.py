import heapq
H = [3, 9, 2, 1, 4, 5]
heapq.heapify (H)
print(H)

heapq.heappush( H, 8)
heapq.heappush( H,10)
heapq.heappush( H,2)
print(H)

heapq.heappop(H)
heapq.heappop(H)
heapq.heappop(H)
heapq.heappop(H)
print (H)
