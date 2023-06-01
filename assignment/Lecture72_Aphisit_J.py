menuList = []

def showBill():
    total_price = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print("menu :",menuList[number][0],end = ' ')
        print("price :",menuList[number][1])
        total_price += int(menuList[number][1])
    print("total price :",total_price)
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])

showBill()