from datetime import datetime

print("---------------------- Welcome --------------------------")
name = input("Enter Your Name :")
#Lists of tuples
lists = '''
rice    Rs 20/kg
sugar   Rs 30/kg
salt    Rs 20/kg
oil     Rs 80/litre
paneer  Rs 110/kg 
maggi   Rs 50/kg 
boost   Rs 90/kg 
colgate Rs 85/each
'''

#Declaration
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist  = []
qlist = []
plist = []
finalamount = 0

#Rates of items
items = {"rice":20,
         "sugar": 30,
         "salt": 20,
         "oil": 80,
         "paneer": 110,
         "maggi": 50,
         "boost": 90,
         "colgate":85
         }

option = int(input("For list of items press 1"))
if option == 1:
    print(lists)

for i in range(len(items)):
    inp1 = int(input("If you want to buy press 1 or 2 for exit"))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter Your Items")
        quantity = int(input("Enter your quantity"))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5) /100
            finalamount = gst + totalprice
        else:
            print("Sorry you entered item is not available")
    else :
        print("You entered wrong number")
    inp = input("Can i bill the items yes or no :")
    if inp == "yes":
        pass
        if finalamount != 0:
            print(29*"=", "Sunny SuperMarket",29*"=")
            print(28*" ","Hyderabad")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*" ")
            print(75 * "-")
            print(3*" ","sno",8*" ","items",8*" ","Quantity",3*" ","price")
            print(75 * "-")
            for i in range(len(pricelist)):
                print(3*" ",i,10*" ",ilist[i],10*" ",qlist[i],10*" ",plist[i])
            print(75*"-")
            print(50*" ","TotalAmount:","Rs",totalprice)
            print("gst amount",50*" ","Rs",gst)
            print(75*"-")
            print(20*" ","Thanks for Visiting")
            print(75*"-")




