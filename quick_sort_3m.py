from statistics import median
import math

counter_3m1 = 0
def quick_sort_3m(A):
    return quick_sort_3m1(A, 0, len(A) - 1, 0)

def quick_sort_3m1(A, p, r, depth):
    global counter_3m1


    if p < r:
        q = partition1(A, p, r)
        quick_sort_3m1(A, p, q - 1, depth+1)
        quick_sort_3m1(A, q + 1, r, depth+1)

    tmp_counter = counter_3m1

    if depth == 0:
        counter_3m1 = 0

    return A, tmp_counter


def partition1(A, p, r):
    if r-p > 3:
        index = A.index(median([A[p], A[r], A[math.floor((p + r) / 2) + 1 ]]))
        A[r], A[index] = A[index], A[r]
    i = p - 1
    global counter_3m1
    for j in range(p, r):
        counter_3m1 += 1
        if A[j] <= A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


print(quick_sort_3m([8, 7, 6, 5, 1, 2, 3, 1,2,1]))  # записувати індекси(від першого до останнього(n - 1))
# print(quick_sort_3m([9, 8, 7, 6, 5, 4, 3, 2]))
