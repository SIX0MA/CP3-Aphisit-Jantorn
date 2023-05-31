def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*0.07)
    return result
inputPrice = int(input("input your price : "))
print("result [price+vat(7%)] :",vatCalculate(inputPrice))