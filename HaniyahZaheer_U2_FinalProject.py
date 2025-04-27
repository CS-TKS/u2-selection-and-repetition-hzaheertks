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
ac_hour = ""

while True: #Experimentation of try/except with Ms. Tellez
    try:
        ac_hour = int(input("How many hours per day do you use air conditioning?"))
        break
    except ValueError:
        print("Please enter a number.")

user_input.append("AC use: "+ str(ac_hour) + "hrs/day")

while True:
    try:
        screen_hour = int(input("How many hours per day do you spend on the screen?"))
        break
    except ValueError:
        print("Please enter a number.")

user_input.append("Screen time: "+ str(screen_hour) + "hrs/day")

energy_emissions = (ac_hour * ac_per_hour + screen_hour * screen_per_hour) *365 / 100 #for metric tonnes / year


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
    waste_emissions = 0.6

else:
    waste_emissions = 1.7


#Storing categories in list
emissions_list = [transport_emissions, food_emissions, waste_emissions] #LATER ADD ENERGY EMISSIONS
categories = ["Transport", "Energy", "Food", "Waste"]

#Finding highest category
highest_emission = 0
highest_category = ""

if transport_emissions > highest_emission:
    highest_emission = transport_emissions
    highest_category = "Transport"

if energy_emissions > highest_emission:
    highest_emission = energy_emissions
    highest_category = "Energy"

if food_emissions > highest_emission:
    highest_emission = food_emissions
    highest_category = "Food"

if waste_emissions > highest_emission:
    highest_emission = waste_emissions
    highest_category = "Waste"

#Output
print("-"*50)
print("Your Eco Report Card!")
print("-"*50)
print(f"Transport emissions: {transport_emissions:.2f} tons CO2 / year")
print(f"Energy emissions: {energy_emissions:.2f} tons CO2 / year")
print(f"Food emissions: {food_emissions:.2f} tons CO2 / year")
print(f"Waste emissions: {waste_emissions:.2f} tons CO2 / year")
print()
print("Your highest source of emissions is...", highest_emission, "!")

#Quiz based on user's highest emission category (questions ChatGPTd)
print("-"*50)
print("Quick quiz time!")
print("-"*50)

if highest_category == "Transport":
    input("How much CO2 does 1 gallon of gas emit?")
    print("Answer: around 8.89 tons")

elif highest_category == ""





#TO DO LIST FORY NEXT CLASS, COMPARE TO KAUST CITIZEN, CREATe SUMMARY, DO QUIZ QUESTIONS, DO CHALLENGE