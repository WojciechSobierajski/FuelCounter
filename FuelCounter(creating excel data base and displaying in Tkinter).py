import openpyxl as xl
wb = xl.load_workbook('TemplateForFuelCounter.xlsx')
sheet = wb['Calculation']
from Functions import FunctionsForFuelCounter
#Beginning
question = ""
car_distance = 0
#creatingnewexcelfile
name = input("What's your name? ")
wb.save(f'{name}.xlsx')
wb = xl.load_workbook(f'{name}.xlsx')
sheet = wb['Calculation']

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
    FunctionsForFuelCounter.displaying_Tkinter(car_distance, distance_driven, total_cost, fuel_consumption)
    FunctionsForFuelCounter.filling_excel(sheet, wb, name, current_distance, current_price, distance_driven, total_cost, current_liters, fuel_consumption, cost_100km)
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
