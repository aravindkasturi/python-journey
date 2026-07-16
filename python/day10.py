#fun with outputs

# def my_fun():
#     result=3*2
#     return result
# print(my_fun())

def format_name(f_name,l_name):
    # f_name=f_name.title()
    # l_name=l_name.title()
    if f_name=="" or l_name=="":
        return  # means if no input it will skip the rest 
    return f"Name is {f_name.title()} {l_name.title()}"
out=format_name(input("Enter first name: "),input("Enter last name: "))
print(out)
