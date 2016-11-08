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

print(insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
