def max_heapify(A, k):
    l = left(k)
    r = right(k) # Correctly passing 'k' to the right function
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)
def left(k):
    return 2 * k + 1
def right(i): # Corrected to use 'i' instead of 'k'
    return 2 * i + 2 # Corrected to use 'i' instead of 'k'
def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A, k)
A = [3, 9, 2, 1, 4, 5]
build_max_heap(A)
print(A)