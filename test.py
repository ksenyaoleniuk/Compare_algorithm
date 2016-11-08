cont = 0
def partition(numbers, start = 0, end = None):
    last = end - 1 if end else len(numbers) - 1

    pivot_value = numbers[last]
    pivot = start
    repetitions = 0
    global cont
    for i in range(start, last):
        value = numbers[i]
        cont += 1
        if value == pivot_value:
            repetitions += 1

        if value <= pivot_value:

            numbers[pivot], numbers[i] = numbers[i], numbers[pivot]
            pivot += 1

    numbers[pivot], numbers[last] = numbers[last], numbers[pivot]
    print(pivot - repetitions // 2)
    return pivot - repetitions // 2

def quicksort(numbers, start = 0, end = None):
    end = end if end else len(numbers)
    global cont
    if start < end - 1:
        pivot = partition(numbers, start, end)
        quicksort(numbers, start, pivot)
        quicksort(numbers, pivot + 1, end)
    return numbers, cont
print(quicksort([1]*8))