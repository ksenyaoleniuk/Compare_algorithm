counter_qs = 0
def quick_sort(A):
    return quick_sort1(A, 0, len(A) - 1,0)
def quick_sort1(A, p, r, depth):
    global counter_qs
    if p < r:
        q = partition_with_equel(A, p, r)
        quick_sort1(A, p, q - 1, depth+1)
        quick_sort1(A, q + 1, r, depth+1)

    tmp_counter = counter_qs
    if depth == 0:
        counter_qs = 0

    return A, tmp_counter

def partition(A, p, r):
    x = A[r]
    i = p - 1
    global counter_qs
    for j in range(p, r):
        counter_qs += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1

def partition_with_equel(A, p, r):
    x = A[r]
    i = p - 1
    comp = 0
    global counter_qs
    for j in range(p, r):
        value = A[j]
        if value == x:
            comp += 1
        counter_qs += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    print("output", "i", i, "comp", comp,  i  - comp //2)
    return i - (comp - 1) //2


print(quick_sort([1,2,3,2,1,2,3]))
print(quick_sort([1]*8))  # записувати індекси(від першого до останнього(n - 1))
