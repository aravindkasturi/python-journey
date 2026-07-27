# control flow

#if-else
# if condition:
#     do this
# else:
#     do this

# water_level=int(input("Enter water level: "))
# if water_level>80:
#     print("Drain water")
# else:
#     print("Continue")

#Modular operator(%)
#gives remainder as output
#10%3==1
# Even num%2 ==0
# a=int(input("Enter num: "))
# if a%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")

#Nested if 
# age=int(input("Enter age: "))
# if age<=18:
#     if age<=7:
#         print("Pay ₹7")
#     else:
#         print("Pay ₹10")
# else:
#     print("Pay ₹15")

#elif
# age=int(input("Enter age: "))
# if age<=7:
#     print("pay ₹7")
# elif age>7 and age<=18:
#     print("pay ₹10")
# else:
#     print("pay ₹15")

# print("Welcome to PIZZAHUT!")
# size=input("What size do you want? S, M, or L: ")
# pepperoni=input("Do you want pepperoni? Y or N: ")
# extra_cheese=input("Do you want extra cheese? Y or N: ")
# bill=0
# if size=='S':
#     bill=15
#     if pepperoni=='Y':
#         bill+=2
#     if extra_cheese=='Y':
#         bill+=1
#     print(f"price is ₹{bill}")
# if size=='M':
#     bill=20
#     if pepperoni=='Y':
#         bill+=3
#     if extra_cheese=='Y':
#         bill+=1
#     print(f"price is ₹{bill}")
# if size=='L':
#     bill=25
#     if pepperoni=='Y':
#         bill+=3
#     if extra_cheese=='Y':
#         bill+=1
#     print(f"price is ₹{bill}")