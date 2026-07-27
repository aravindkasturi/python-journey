#classes --blue print
class User:   #class name should be in PascalCase
    def __init__(self,id,username):  #constructor -- initialise attributes
        self.id=id
        self.username=username
        self.followers=0
    #methods

        
user_1 = User("001","aravind")
user_2 = User("002","virat")
print(user_2.followers)
#attributes --- properties  or variable associated with objects