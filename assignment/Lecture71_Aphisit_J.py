menuList = []
priceList = []

def showBill():
    total_price = 0
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        total_price += int(priceList[number])
        if number == (len(menuList))-1:
            print("---------------")
            print("total price : ",total_price)

while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()