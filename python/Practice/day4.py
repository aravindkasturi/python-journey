#Random Module

import random 
# print(random.randint(10,20))  -integers 
# print(random.random()) -floating from 0 to 1
#random.uniform(a,b) --floating including both a and b

# a=random.randint(0,1)
# if a==0:
#     print("Tails")
# else:
#     print("Heads")

#lists
# a=[1,"AK",True,1+3j,3.5]
# print(a[0]) --> 1 <-- a[-1]
# a.append("VK") --> appends single item at the end of the list
#extend --> adds bunch of item not need to be only list it can be tuple also

a=input("Enter names: ").split()
b=len(a)
print(a[random.randint(0,b)])

