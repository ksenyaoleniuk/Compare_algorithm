def counting_sort(A, k): #k - максимальне значення елементу
    B = [0] * (len(A))
    C = [0] * (k + 1) # k + 1 тому що ще нуль
    for i in range(0, len(A)):
        C[A[i]] += 1
    for j in range(1, k + 1):
        C[j] = C[j] + C[j - 1]

    # for l in range(len(A) - 1, -1 , -1):
    for l in range(0, len(A)):

        B[C[A[l]] - 1] = A[l]
        C[A[l]] -= 1
    return B
print(counting_sort([1,2,1,3,2,4,3,4,5], 5))