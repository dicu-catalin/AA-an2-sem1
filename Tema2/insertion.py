def insertionSort(l):
    length = len(l)
    for i in range(1, length):
        key = l.pop(i)
        j = i
        while j > 0 and l[j-1] > key:
            j -= 1
        l.insert(j, key)