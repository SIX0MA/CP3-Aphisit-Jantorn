floor = int(input("input : "))
space_index = floor-1
print("output")

for i in range(floor):
    print(" "*(space_index)+"*"*(2*i+1))
    space_index -= 1
