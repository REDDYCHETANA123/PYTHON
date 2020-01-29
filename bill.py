name=input("enter your name")
board=input("enter your boarding place")
dest=input("enter your destinaton place")
kilo=input("enter the number of kilometres you want to travel")
faci=int(input("enter facility \n  1.normal \n,2.delux \n 3.superdelux \n 4.ultra delux"))
price=0
if(faci==1):
    price=km*6
elif(faci==2):
    price=km*8
elif(faci==3):
    price=km*12
elif(faci==4):
    price=km*15
else:
    print("enter correct option")
print("name:",name)
print("board:",board)
print("detionation:",dest)
print("date of journey:",date)
print("travel of distance:",km)
print("total price:",price)
