weight = int(input("enter your weight : "))
unit = input("(L)bs or (K)g : ")
if unit == "L":
    print(weight * 2.20462)
elif unit == "K":
    print(weight / 2.20462)
else:
    print("invalid input")
