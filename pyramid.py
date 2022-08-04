"""
a = 1
b = 10
while a <= 10 and b >= 1:
    print((" " * b) + ("*" * a) + (" " * b))
    a += 1
    b -= 1
"""

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print("* ", end="")
        k += 1

    k = 0
    print()