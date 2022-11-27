
def selectionSort(array):
    i = 0
    while i < len(array) - 1:
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j += 1
        array[i], array[m] = array[m], array[i]
        i += 1