
# Encapsulation

class Dog:
    def __init__(self,name,breed):
        self.__name = "chopper"
        self.breed = "dobber"
    
    def set_dog_name(self,name):
        self.__name = name
        
    def get_dog_name(self):
        return self.__name
    

dog = Dog()
dog.set_dog_name("luffy")  
print(dog.get_dog_name()) 



  