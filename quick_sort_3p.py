
def quick_sort_3p(A):
    return partition(A, 0, len(A) - 1)


def partition(A, left, right):
    counter_qs_3p = 0
    a = left + 2
    b = left + 2
    c = right - 1
    d = right - 1
    p = A[left]
    q = A[left + 1]
    r = A[right]
    while b <= c:
        counter_qs_3p += 1
        while A[b] < q and b <= c:
            counter_qs_3p += 1
            if A[b] < p:
                A[a], A[b] = A[b], A[a]
                a += 1

            b += 1
        while A[c] > q and b <= c:
            counter_qs_3p += 1
            if A[c] > r:
                A[c], A[d] = A[d], A[c]
                d -= 1
            c -= 1

        if b <= c:
            counter_qs_3p += 1
            if A[b] > r:
                if A[c] < p:
                    A[b], A[a] = A[a], A[b]
                    A[a], A[c] = A[c], A[a]
                    a += 1
                else:
                    A[b], A[c] = A[c], A[b]

                A[c],A[d] = A[d], A[c]
                b += 1
                c -= 1
                d -= 1
            else:
                if A[c] < p:
                    A[b], A[a] = A[a], A[b]
                    A[a], A[c] = A[c], A[a]
                    a += 1
                else:
                    A[b], A[c] = A[c], A[b]
                b += 1
                c -= 1
    a -= 1
    b -= 1
    c += 1
    d += 1
    A[left + 1], A[a] = A[a], A[left + 1]
    A[a], A[b] = A[b], A[a]
    a -= 1
    A[left], A[a] = A[a], A[left]
    A[right], A[d] = A[d], A[right]
    return A, counter_qs_3p

print(quick_sort_3p([1,2,3,1,2]))