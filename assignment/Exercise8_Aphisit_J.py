#User data
user_name = input("username : ")
user_password = input("password : ")
cost = 0
if user_name == "user1" and user_password == "user1_1234":
    print("--------Welcome to 1234 SHOP--------")

    print("   Product    cost(THB)    number")
    print("   banana            10         1")
    print("   egg                6         2")
    print("   bread             22         3")
    print("   tomato             7         4")
    print("   apple             15         5")

    print("------------------------------------")

    product_number = int(input("Which product do you want to buy (Key in number) : "))
    amount = int(input("How many product do you want to buy (Key in number) : "))

    if product_number == 1 :
        cost = 10*amount
    elif product_number == 2 :
        cost = 6*amount
    elif product_number == 3 :
        cost = 22*amount
    elif product_number == 4 :
        cost = 7*amount
    elif product_number == 5 :
        cost = 15*amount
    else:
        print()
        print("None")

    print("------------------------------------")
    print("Total cost :",cost,"THB")
else:
    print("ERROR")