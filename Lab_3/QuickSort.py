import random

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
        l = []
        m = []
        r = []
        for elem in array:
            if elem < q:
                l.append(elem) 
            elif elem > q: 
                r.append(elem) 
            else: 
                m.append(elem)
        return quickSort(l) + m + quickSort(r)