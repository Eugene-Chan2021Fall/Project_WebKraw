from collections import defaultdict

def sortFreq(array, m):
    hsh = defaultdict(lambda: 0)
    for i in range(m):
        hsh[array[i]] += 1
    array.sort(key=lambda x: (x,-hsh[x]))
    return (array)
 
 
price = []
price = [int(item) for item in input("Sorted Price: ").split()]
m = len(price)   
sol = sortFreq(price, m)
print(*sol)
