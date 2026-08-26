#FileNotFoundError
# with open("a_file","r") as f:
#     f.read()

#KeyError
# a={"ak":68,"vk":18}
# print(a["ck"])

#IndexError
# fruit_list=["Apple","Grape","Banana"]
# print(fruit_list[3])

#TypeError
# print("Ak"+2)

#Exception Handling
# try:    #code that might cause exception
#     pass
# except:  #if exception do this
#     pass
# else:   #if no exception do this
#     pass
# finally: #no matter what do this
#     pass
# raise KeyError #Raising error manually

try:
    file=open("a_file","r")
except FileNotFoundError:
    file=open("a_file","w")
    file.write("AK")
else:
    file.read()
finally:
    print("END")
    file.close()
