from collections import deque
import random

BUCKETS = 10
DIGITS = 4

def radix_sort(A):
    queues = []
    
    # BUCKETS는 진수에 따라 결정 (10진수 -> BUCKETS = 10)
    for i in range(BUCKETS):
        queues.append(deque())

    n = len(A)
    factor = 1

    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i]//factor) % BUCKETS].append(A[i])
        
        i = 0
        for b in range(BUCKETS):
            while queues[b]:
                A[i] = queues[b].popleft()
                i += 1
        
        factor *= BUCKETS
        print("step", d + 1, A)

data = [random.randint(1, 9999) for _ in range(10)]
radix_sort(data)

print("Radix : ", data)