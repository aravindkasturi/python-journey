#snake game project Day2

#4. Detect collision with food

#5. create score board

#6. detect collision with wall

#7. detect collision with tail


#class inheritence
#one class accquires the properties and methods of another class
class Animal:
    def __init__(self):
        self.num_eyes=2
    def breathe(self):
        print("Inhale, Exhale")
class Fish(Animal):
    def __init__(self):
        """when object created it searches for init here super().__init__() says refer to parent init"""
        super().__init__()
    def breathe(self):
        super().breathe()
        print("doing underwater")
    def swim(self):
        print("moving in water")
fish1=Fish()
fish1.breathe()
print(fish1.num_eyes)
fish1.breathe()