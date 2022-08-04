a = int(input("Enter yur guess : "))
if a == 30:
    print("Your guess is correct")
elif a > 30:
    print("Guess lower")
elif a < 30:
    print("Guess higher")