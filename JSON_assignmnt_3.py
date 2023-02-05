

class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color


    def description(self):
        print(f"{self.name} is {self.age} years old .")    


    def get_info(self):
        print(f"The coat color of {self.name} is {self.coat_color}")  



class JackRussellTerrior(Dog):
    def __init__(self, name, age, coat_color, breed, energy_lvl):
        Dog.__init__(self, name, age, coat_color)   
        self.breed = breed
        self.energy_lvl = energy_lvl

    def breed_info(self):
        print(f"{self.name} is a {self.breed} breed")

    def energy_lvl_info(self):
        print(f"{self.name} has {self.energy_lvl} energy level")



class Bull_dog(Dog):
    def __init__(self, name, age, coat_color, breed, friendly_lvl):
        Dog.__init__(self, name, age, coat_color)
        self.breed = breed
        self.friendly_lvl = friendly_lvl


    def breed_info(self):
        print(f"{self.name} is a {self.breed} breed")

    def friendly_lvl_info(self):
        print(f"{self.name} has friendly level of {self.friendly_lvl} .")



Dog1 = JackRussellTerrior("TOMY", 3, "BLACK", "JACK RUSSEL TWRRIER", "HIGH")
Dog2 = Bull_dog("bullu", 5, "white", "BULL DOG", "KHATARNAK") 

#calling all my methodsss

Dog1.description()
Dog1.get_info()
Dog1.breed_info()
Dog1.energy_lvl_info()

print("\n \n")

Dog2.description()
Dog2.get_info()
Dog2.breed_info()
Dog2.friendly_lvl_info()





