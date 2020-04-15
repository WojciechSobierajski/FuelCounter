import openpyxl as xl
from datetime import datetime
wb = xl.load_workbook('TemplateForFuelCounter.xlsx')
sheet = wb['Calculation']

#Defined functions
def displaying_calculated():
    dist=f'Przejechałeś: {distance_driven} km'
    print(dist)
    trip_cost = f'Kosztowało Cię to: {total_cost} zł'
    print(trip_cost)
    liters_per_100km= f'Spalanie na 100km wyniosło: {fuel_consumption} l/100 km'
    print(liters_per_100km)
    print(f'Przebieg Twojego samochodu wynosi: {car_distance}km')


def displaying_validation_of_style():
    if fuel_consumption > 10:
        print('Za ciężka noga!')
    if fuel_consumption < 10 and fuel_consumption > 5:
        print('Spalanie w normie!')
    if fuel_consumption < 5:
        print('...Bardzo mało !')
        cost_of_100km = f'Czyli za 100 km zapłaciłeś: {cost_100km} zł'
        print(cost_of_100km)


def filling_excel():
    cell = sheet.cell(sheet.max_row + 1, 1)
    cell.value = (datetime.date(datetime.now()))
    cell = sheet.cell(sheet.max_row, 2)
    cell.value = current_distance
    cell = sheet.cell(sheet.max_row, 3)
    cell.value = current_price
    cell = sheet.cell(sheet.max_row, 4)
    cell.value = current_liters
    cell = sheet.cell(sheet.max_row, 5)
    cell.value = distance_driven
    cell = sheet.cell(sheet.max_row, 6)
    cell.value = total_cost
    cell = sheet.cell(sheet.max_row, 7)
    cell.value = fuel_consumption
    cell = sheet.cell(sheet.max_row, 8)
    cell.value = cost_100km
    wb.save(f'{name}.xlsx')


#Beginning
question = ""
car_distance = 0
name = input("What's your name? ")
wb.save(f'{name}.xlsx')
wb = xl.load_workbook(f'{name}.xlsx')
sheet = wb['Calculation']
print(f'Hey {name}, welcome to my Fuel Counter! Have fun and calculate.')

while question != "yes":
# input_from_user
    current_distance = input('Bieżący stan licznika (km) ')
    current_price = input('Cena za litr ')
    current_price = current_price.replace('.','').replace(',','.')
    current_liters = input('Ile litrów? ')
#calculation
    distance_driven = int(current_distance) - int(car_distance)
    total_cost = float(current_price) * float(current_liters)
    fuel_consumption = round((float(current_liters) / float(distance_driven) * 100), 2)
    cost_100km = round(float(fuel_consumption * float(current_price)), 2)
    car_distance += int(distance_driven)
#Executing fuctions
    displaying_calculated()
    displaying_validation_of_style()
    filling_excel()
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
