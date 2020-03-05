def quicksort(array):
    if len(array) < 2:
        return array
    else:
        index = len(array) // 2
        pivot = array[index]
        less = []
        for i in array[0:index] + array[1 + index:]:
            if i <= pivot:
                less.append(i)
        greater = []
        for i in array[0:index] + array[index:]:
            if i > pivot:
                greater.append(i)
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([1, 10, 3, 8, 5, 2, 0, 13, 6, 1, 10, 3, 8, 5, 2, 0, 13, 6]))