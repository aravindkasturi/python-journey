#files

# file=open("my_file.txt")   # to open a file
# contents=file.read()       #reading a file
# print(contents)
# file.close()               #to close cuz when we open it take some of resources and to close them 
                            

#same as above without close() but it will close automatically
# with open("my_file.txt") as file:
#     contents=file.read()
#     print(contents)

#write
# with open("my_file.txt",mode="a") as file:
#     file.write("\nMy name is Aravind")

#when we try to open a file in w mode and if that file doesnt exist it will create if only in write mode
# with open("new_file.txt",mode="w")as file:
#     file.write("New file")


