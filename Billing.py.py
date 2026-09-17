from datetime import datetime
name = input("Enter Customer Name: ") 

# lists of items
lists='''
Rice    Rs 25/kg
Sugar   Rs 5/kg
Salt    Rs 10/kg
Oil     Rs 20/liter
Paneer  Rs 100/kg
Maggi   Rs 32/kg
Boost   Rs 50/each
Colgate Rs 90/each
'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':25,
       'sugar':5,
       'salt':10,
       'oil':20,
       'paneer':100 ,
       'maggi':32,
       'boost':50,
       'colgate':90}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input(" Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0: 
            print(33*"=","Praveen MART",33*"=")
            print(66*" "," CHITTOOR")
            print( "Name:",name,20*" ","Date:", datetime.now().strftime("%d/%m/%Y  Time: %I:%M"))
            print(75*"-")
            print(f"{'SNo':<5}{'Item':<15}{'Quantity':>10}{'Price':>14}")
            for i in range(len(pricelist)):
             print(f"{i+1:<5}{ilist[i]:<13}{qlist[i]:>7}{plist[i]:>19}")
            print(75*"-")
            print(50*" ",' TotalAmount:','Rs',totalprice)
            print(32*"=","Thanks for visiting",30*"=")