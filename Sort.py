import pandas as pd

#A class to represent a Nike Air Force 1 Shoe
class AirForceOne:
   def __Init__(self,name,price,type):
       self.name_ = name
       self.price_ = price
       self.type_ = type
    
   def __le__(self,rhs):
       return self.price_ <= rhs.price_
    
   def __lt__(self,rhs):
       return self.price_ <= rhs.price_
    
   def display(self):
       return format(self.name_,'100') + "$" + format(self.price_,'.2f')
       

#quickSort sorts in place
def quickSort(A,start,end) :
    if start < end:
        pIndex = Partition(A,start,end)
        quickSort(A,start,pIndex-1)
        quickSort(A,pIndex+1,end)

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def Partition(A,start,end):
    pIndex = start
    pivot = end
    for element in range(start,end):
        if A[element] <= A[pivot]:
            swap(A,element,pIndex)
            pIndex = pIndex + 1

    swap(A,end,pIndex)
    return pIndex

#mergeSort returns a sorted list
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


#open csv file with pandas
nike = pd.read_csv("nike.csv")
ebay = pd.read_csv("ebay.csv")


#get the Name, Price, and Type columns and store them into separate lists
nike_name = list(nike.Name)
nike_price = list(map(float,nike.Price)) # convert each string type to float type
nike_type = list(nike.Type)


ebay_name = list(ebay.Name)
ebay_price = list(ebay.Price)
ebay_type = list(ebay.Type)


# remove irrelavent data from ebay_price
for x in range(1,len(ebay_price)):
    if len(ebay_price[x]) > 6:
        ebay_price[x] = ebay_price[x][:6]

ebay_price = list(map(float,ebay_price)) # convert each string type to float type


#create a list of uninitialized AirForceOne objects
shoe_list =  [AirForceOne() for i in range(len(nike_name + ebay_name)-1)]

#Initialize each AirForceOne object
for i in range(1,len(ebay_name)):
    shoe_list[i-1].name_ = ebay_name[i]
    shoe_list[i-1].type_ = ebay_type[i]
    shoe_list[i-1].price_ = ebay_price[i]

j = 0
for i in range(len(ebay_name)-1,len(shoe_list)):
    shoe_list[i].name_ = nike_name[j]
    shoe_list[i].type_ = nike_type[j]
    shoe_list[i].price_ = nike_price[j]
    j = j + 1

#mergeSort returns a sorted list
shoe_list_ms = mergeSort(shoe_list) 
#quickSort sorts in place
quickSort(shoe_list,0,len(shoe_list)-1)


#test
print("\nQuickSort:")

for i in range(len(shoe_list)):
    print(shoe_list[i].display())

print("\nMergeSort:")
for i in range(len(shoe_list)):
   print(shoe_list_ms[i].display())
