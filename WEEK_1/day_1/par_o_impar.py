number = int(input("WRITE A NUMBER, then press enter to continue:"))

modular = number%2

print(modular)

if number%2 == 0:
    print("Your number is even")
else:
    print("your number is odd")
