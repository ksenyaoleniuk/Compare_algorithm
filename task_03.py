from statistics import median
import math

#insertion sort
def insertion_sort(mylist):
    counter = 0
    for j in range(1, len(mylist)):

        key = mylist[j]
        i = j - 1

        while mylist[i] > key and i >= 0:
            mylist[i + 1] = mylist[i]
            i = i - 1
            counter += 1
        counter += 1
        mylist[i + 1] = key
    return mylist, counter

# merge sort
counter_ms = 0

def merge_sort(A):
    return merge_sort_main(A, 0, len(A), 0)

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
    global counter_ms
    n1 = q - p
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
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

# quick sort
counter_qs = 0

def quick_sort(A):
    return quick_sort1(A, 0, len(A) - 1,0)

def quick_sort1(A, p, r, depth):
    global counter_qs
    if p < r:
        q = partition(A, p, r)
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

# quick sort with 3 pivots
counter_3m1 = 0
def quick_sort_3m(A):
    return quick_sort_3m1(A, 0, len(A) - 1, 0)

def quick_sort_3m1(A, p, r, depth):
    global counter_3m1
    if p < r:
        q = partition1(A, p, r)
        quick_sort_3m1(A, p, q - 1, depth + 1)
        quick_sort_3m1(A, q + 1, r, depth + 1)
    tmp_counter = counter_3m1
    if depth == 0:
        counter_3m1 = 0
    return A, tmp_counter

def partition1(A, p, r):
    if r - p > 3:
        index = A.index(median([A[p], A[r], A[math.floor((p + r) / 2)]]))
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
