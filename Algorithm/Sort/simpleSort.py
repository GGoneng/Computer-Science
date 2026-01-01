def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if (A[j]<A[least]):
                least = j
        A[i], A[least] = A[least], A[i]

        print(f"Step {i + 1:2d} = {A}")

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

if __name__ == "__main__":
    data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
    print("Original : ", data)
    selection_sort(data)
    print("Selection : ", data)