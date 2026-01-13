def sequential_search(A, key, low, high):
    for i in range(low, high + 1):
        if A[i] == key:
            return i
    return -1

def sequential_search_transpose(A, key, low, high):
    for i in range(low, high + 1):
        if A[i] == key:
            if i > low:
                A[i], A[i - 1] = A[i - 1], A[i]
                i = i - 1
            return i
    return -1

def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif (key < A[middle]):
            return binary_search(A, key, low, middle - 1)
        else:
            return binary_search(A, key, middle + 1, high)
    
    return -1

def binary_search_iter(A, key, low, high):
    while (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif (key > A[middle]):
            low = middle + 1
        else:
            high = middle - 1
    
    return -1

def interpolation_search(A, key, low, high):
    if (low <= high):
        middle = int(low + (high - low) * (key - A[low].key) / (A[high].key - A[low].key))
        if key == A[middle]:
            return middle
    elif (key < A[middle]):
        return interpolation_search(A, key, low, middle - 1)
    else:
        return interpolation_search(A, key, middle + 1, high)
    
    return -1

