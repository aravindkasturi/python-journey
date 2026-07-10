print("Welcome to the tip Caluculator!")
a=float(input("What was the total bill? ₹ "))
b=float(input("How much tip would you like to give? ₹"))
b=(b/100)*a
print(b)
c=int(input("How many people to split the bill?"))
d=(a+b)/c
print(f"Each person should pay ₹{d}")

