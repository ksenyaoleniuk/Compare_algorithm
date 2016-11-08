import math
counter_ms = 0

def merge_sort(A):
    return  merge_sort_main(A, 0, len(A), 0)


def merge_sort_main(A, p, r, depth):
    global counter_ms

    if r - p > 1:
        merge_sort_main(A, p,(p + r)//2, depth + 1)
        merge_sort_main(A, (p + r)//2, r, depth + 1)
        merge(A, p,(p + r)//2,  r)

    tmp_counter = counter_ms

    if depth == 0:
        counter_ms = 0

    return A, tmp_counter
def merge(A, p, q, r):
    n1 = q - p
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    global counter_ms

    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j]
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    for k in range(p, r):
        counter_ms += 1

        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:

            A[k] = R[j]
            j += 1

    return A

print(merge_sort([i for i in range(10)]))


