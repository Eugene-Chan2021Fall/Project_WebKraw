import pandas as pd

#A class to represent a Nike Air Force 1 Shoe
class AirForceOne:
   def __Init__(self,name,price,type):
       self.name_ = name
       self.price_ = price
       self.type_ = type
    
   def __le__(self,rhs):
       return self.price_ <= rhs.price_
    
   def display(self):
       print("Name:",self.name_,"\nPrice:",self.price_," \nType:",self.type_,"\n---")


#open csv file with pandas
nike = pd.read_csv("nike.csv")
ebay = pd.read_csv("ebay.csv")


#get the Name, Price, and Type columns and store them into separate lists
nike_name = list(nike.Name)
nike_price = list(map(float,nike.Price))
nike_type = list(nike.Type)

ebay_name = list(ebay.Name)
ebay_price = list(ebay.Price)
ebay_type = list(ebay.Type)



# remove irrelavent data from ebay_price
for x in range(1,len(ebay_price)):
    if len(ebay_price[x]) > 6:
        ebay_price[x] = ebay_price[x][:6]

ebay_price = list(map(float,ebay_price))

#create a list of uninitialized AirForceOne objects
nike_list =  [AirForceOne() for i in range(len(nike_name))]
ebay_list =  [AirForceOne() for i in range(len(ebay_name)-1)]


#Initialize each AirForceOne object
for i in range(len(nike_name)):
    nike_list[i].name_ = nike_name[i]
    nike_list[i].type_ = nike_type[i]
    nike_list[i].price_ = nike_price[i]

for i in range(1,len(ebay_name)):
    ebay_list[i-1].name_ = ebay_name[i]
    ebay_list[i-1].type_ = ebay_type[i]
    ebay_list[i-1].price_ = ebay_price[i]

#test  
for i in range(len(ebay_name)-1):
    print(vars(ebay_list[i]))
    #print(ebay_list[i].display())
for i in range(len(nike_name)):
    #print(nike_list[i].display())
    print(vars(nike_list[i]))

    

