
# animals = ["cat", "dog", "monkey", "cow"]

# combined = []


# for i in range(len(animals)):
#     current_animal = animals[i]
#     next_animal = animals[(i+1) % len(animals)]
#     combined = current_animal + next_animal[:2]
#     print(combined)
    


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