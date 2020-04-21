from Functions import FunctionsForFuelCounter
#Beginning
question = ""
car_distance = 0
name = input("What's your name? ")
print(f'Hey {name}, welcome to my Fuel Counter! Have fun and calculate.')

while question != "yes":
# input_from_user
    current_distance = input('Current state of odometer (km) ')
    current_price = input('Price of 1 liter of gasoline ')
    current_price = current_price.replace(',', '.')
    current_liters = input('How much liters did you fill? ')
    current_liters = current_liters.replace(',', '.')
#calculation
    distance_driven = int(current_distance) - int(car_distance)
    total_cost = round(float(current_price) * float(current_liters), 2)
    fuel_consumption = round((float(current_liters) / float(distance_driven) * 100), 2)
    cost_100km = round(float(fuel_consumption * float(current_price)), 2)
    car_distance += int(distance_driven)
#Executing fuctions
    FunctionsForFuelCounter.displaying_calculated(distance_driven, total_cost, cost_100km, fuel_consumption)
    FunctionsForFuelCounter.displaying_validation_of_style(fuel_consumption)
#loop question
    question = input("Are we finished? Yes or No? ").lower()
    if question == "yes":
        print("Thanks for using it! ")
        break
    if question == "no":
        print("Ok, let's go once again ")
    else:
        print("You were supposed to say Yes or No :P")
        question = input("Are we finished? Yes or No? ").lower()