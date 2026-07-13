#day5 - For loops, Range and code blocks

# for loop
# for item in range(0,n+1):
#     statements

# fruits=["Apple","guava","orange"]
# for fruit in fruits:
#     print(fruit)

# a=[1,2,3,4,5]
# print(sum(a))

for i in range(0,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i %5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)