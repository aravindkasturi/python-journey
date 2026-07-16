# #fun with outputs

# # def my_fun():
# #     result=3*2
# #     return result
# # print(my_fun())

# def format_name(f_name,l_name):
#     # f_name=f_name.title()
#     # l_name=l_name.title()
#     if f_name=="" or l_name=="":
#         return  "You havent provided input"# means if no input it will skip the rest 
#     return f"Name is {f_name.title()} {l_name.title()}"
# out=format_name(input("Enter first name: "),input("Enter last name: "))
# print(out)

#Leap Year
def is_leap(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False
out=is_leap(int(input("Enter year: ")))
print(out)