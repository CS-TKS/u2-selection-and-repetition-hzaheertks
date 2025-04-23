#Eco report card program
#@Author Haniyah Zaheer


#Welcome
print("-"*70)
user = input("Welcome! What is your name?")
name = user.capitalize()
print("Welcome to your personalized Eco Report Card," , name, " — a fun and eye-opening way to discover how your daily choices impact the planet, " , name, ". ")
print("Let’s explore your habits and see where you shine… and where there’s room to grow a little greener!")

print("Let's dive right in," , name, "!")
print("-"*70)
print("Please enter the respective values below to calculate your total carbon emissions per year.")
print("-"*70)
print()

#List storing user inputs
user_input = []

#Constant values for each category (according to Crit A research)
#Transportation
car = 4.6
bike = 0.0
walk = 0.0
bus = 1.8

#Energy consumption
ac_per_hour = 1.2
screen_per_hour = 0.4

#Food
vegetarian = 1.7
meat = 3.3
mixed = 2.5

#Waste
recycle = 0.6
recycle_not = 1.7

#Collecting input emissions (TRANSPORT)
transport = ""
while transport != "car" and transport != "bike" and transport != "bus" and transport != "walk":
    transport = input("What is your main mode of transport when going to school? (walk, bus, bike, car): ").lower()

user_input.append("Transport: " + transport)

#assiging emissions
if transport == "car":
    transport_emissions = car

elif transport == "bus":
    transport_emissions = bus

else:
    transport_emissions = 0.0


#Collecting input emissions (ENERGY CONSUMPTION)
#need to use try/except here - do a bit more research before working on this COME BACK TO THIS


#Collecting input emissions (FOOD)
food = ""

while food != "vegetarian" and food != "mixed" and food != "meat":
    food = input("What does your diet mainly consist of? (vegetarian, mixed, meat): ").lower()

if food == "vegetarian":
    food_emissions = vegetarian

elif food == "mixed":
    food_emissions = mixed

elif food == "meat":
    food_emissions = meat

user_input.append("Diet: " + food)


#Collecting input emissions (WASTE)
recycle = ""
while recycle != "yes" and recycle != "no":
    recycle = input("Do you recycle regularly (yes/no): ").lower()

if recycle == "yes":
    waste_emissions = recycle

else:
    waste_emissions = recycle_not

#TO DO LIST FOR NEXT CLASS, COMPARE TO KAUST CITIZEN, DO ENERGY CONSUMPTION SECTION, CREATe SUMMARY, DO QUIZ QUESTIONS, DO CHALLENGE