def mergeSort(priceList):
    length = len(priceList)
    if length==1:
        return priceList

    midpoint = length // 2
    Left = mergeSort(priceList[:midpoint])
    Right = mergeSort(priceList[midpoint:])

    return merge(Left, Right)

def merge(first, second):
    i = 0
    j = 0
    result = []
    while i<len(first) and j<len(second):
        if first[i]<second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    if i<len(first):
        result.extend(first[i:])
    if j<len(second):
        result.extend(second[j:])
    return result

#Testing
priceBank = [11.3, 100.83, 150, 11.5, 542, 543, 130.03, 30, 23, 830.43]
print(mergeSort(priceBank))
