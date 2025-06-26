# 1. output = catdo, dogmo, monkeyco, cowca

animals = ["cat", "dog", "monkey", "cow"]

combined = []


for i in range(len(animals)):
    current_animal = animals[i]
    next_animal = animals[(i+1) % len(animals)]
    combined = current_animal + next_animal[:2]
    print(combined)
    

# 2

class Tv:
    def turn_on(self):
        print("Tv is turned on now")
    
    def turn_off(self):
        print("Tv is turned off now")

class Remote:
    def __init__(self):
        self.tv = Tv()  
    
    def press_power_on(self):
        self.tv.turn_on()
        
    def press_power_off(self):
        self.tv.turn_off()

remote = Remote()
remote.press_power_on()
remote.press_power_off() 

# 3

class Engine:
    def  start_engine(self):
        print("your car is started now...")
        
    def stop_engine(self):
        print("your car is stoped now..")    

class Car:
    def __init__(self):
        self.engine = Engine()
        
    def start_car(self):
        self.engine.start_engine()
    
    def stop_car(self):
        self.engine.stop_engine()  
        
car = Car()

car.engine.start_engine()  
car.engine.stop_engine()   


# 4 
 
class Room:
    def __init__(self):
        self.light = Light()
        
    def room_light_switch_on(self):
        self.light.turn_on() 
        
    def room_light_switch_off(self):
        self.light.turn_off()       

class Light:
    def turn_on(self):
        print("light is turned on now...")
        
    def turn_off(self):
        print("light is turned off now")
  

room = Room()
room.room_light_switch_on()  
room.room_light_switch_off() 

# 5.

class Laptop:
    def __init__(self):
        self.battery = Battery()
        
    
    
class Battery:
    def check_charge(self,charge):
        
        if charge :
            print("laptop is charging")  
            
        else:
            print("laptop is not charging")    
        

laptop = Laptop()
laptop.battery.check_charge(True) 



 
6.

class Camera:
    def take_a_picture(self):
        print("Give a smile! picture is clicking")   
        
        
class Moblie:
    def __init__(self):
        self.camera = Camera()


moblie = Moblie()
moblie.camera.take_a_picture()
                                                             