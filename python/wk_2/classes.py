# class Vehicle:
#     def __init__(self, name, category="sport", wheels=4):
#         self.name = name
#         self.category = category
#         self.wheels = wheels
    
# gtr = Vehicle("Nissan GTR")
# jeep = Vehicle("Grand Cherokee", "SUV")
# yamaha = Vehicle("Yamaha R1", "motorcycle", 2)
# sierra = Vehicle("GMC Sierra", "truck")
# gsxr = Vehicle("Suzuki", "motorcyle", 2)

# vehicles = [gtr, jeep, yamaha, sierra, gsxr]
# for vehicle in vehicles:
#     print("Name: %s | Type: %s | Wheels: %i" % 
#     (vehicle.name, vehicle.category, vehicle.wheels))

# Alternative --------- NOT Preferred way -------------    
# print(gtr.name, gtr.category, gtr.wheels)
# print(jeep.name, jeep.category, jeep.wheels)
# print(yamaha.name, yamaha.category, yamaha.wheels)
# print(sierra.name, sierra.category, sierra.wheels)
# print(gsxr.name, gsxr.category, gsxr.wheels)


# Exercise 2
class Vehicle:
    def __init__ (self, top_speed, acceleration, wheels=4):
        self.wheels = wheels
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.speed = 0
        self.position = 0
    
    def move(self, move):
        self.accelerate
        self.position += self.speed

    def accelerate(self, acceleration):
        self.speed += acceleration
        if self.speed >= self.top_speed:
            self.speed = self.top_speed #self.speed NOT accelerate

# gtr = Vehicle()
# jeep = Vehicle()
yamaha = Vehicle(180, 5, 2)
# sierra = Vehicle()
gsxr = Vehicle(180, 4, 2)

# motorcycles = [yamaha, gsxr] 

#Alternative use a dictionary
motorcycles = {
"yamaha": Vehicle(180,5,2),
"gsxr": Vehicle(180,4,2),
"sierra": Vehicle(60,3)
}

print("20 second run")
i = 0
while i < 20:
    for motorcycle in motorcycles:
        cur_move = motorcycles[motorcycle].move()
        print("%s - %i" %(motorcycle, motorcycle.speed))
    i +=1
for motorcycle in motorcycles:
    print("")


# sec = 0
# while sec < 60:
#     vehicles = [gtr, jeep, yamaha, sierra, gsxr]
#     for vehicle in vehicles:
#         vehicle.move += 1
#     sec += 1

# while sec < 40:
#     vehicles = [gtr, jeep, yamaha, sierra, gsxr]
#     for vehicle in vehicles:
#         vehicle.move += 1
#     sec += 1

# while sec < 20:
#     vehicles = [gtr, jeep, yamaha, sierra, gsxr]
#     for vehicle in vehicles:
#         vehicle.move += 1
#     sec += 1