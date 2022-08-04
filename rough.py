rows = int(input("Enter the number of rows for the pattern: "))
typeOfP = bool(int(input("Enter 0 or 1: ")))
if typeOfP:
    i = 1
    while i <= rows:
        print(i * "*")
        i += 1
else:
    i = rows
    while rows >= i > 0:
        print(i * "*")
        i -= 1
