# a = 5
# for a in range(5):
#    print("*" * (a+1))


a = int(input("enter your number: "))
b = 1
while a >= 1 and b <= 100:
    print((" " * b) + ("*" * a))
    a -= 1
    b -= 1

c = int(input("enter your number: "))
d = 1
while c >= 1 and d <= 100:
    print((" " * c) + ('*' * d))
    c -= 1
    d += 1
