#debugging - process of removing bugs from code
#steps

#1 describe the problem
# def my_fun():
#     for i in range(0,20): #fix is 0,21
#         if i ==20:
#             print("you got it") #we wont get output as range is upto 19
# my_fun()

#describe the problem - write your answers as comments:
#1.what is the for loop doing?
#2.when is the function meant to print "you got it"?
#3.what are the assumptions about the value of i?

#2. Reproduce the bug
# from random import randint
# dice_images=[1,2,3,4,5,6]
# dice_num=randint(1,6) #fix is 0-5
# print(dice_images[dice_num])
# some times we produce error cuz the index values of dice_image is 0-5
#but if dic_num produces 6 as index it will give list index out of range

#3. Fix the errors that redlines we got
# def my_fun():
# hi #here we got indentation error in red line

# try:
#     age=int(input("Enter age: "))
# except ValueError:
#     print("You have to type integer")
# finally:
#     print(f"your age is {age}")

