import tkinter as tk
from datetime import datetime


def displaying_Tkinter(car_distance, distance_driven, total_cost, fuel_consumption):
    def closing():
        root.destroy()
    root = tk.Tk()
    canvas = tk.Canvas(root, height=300, width=400, bg="dark red")
    canvas.pack()
    frame = tk.Frame(root, height=100, width=100, bg="brown")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    label = tk.Label(frame, text=(f"You've driven: {distance_driven} km"))
    label.place(relx=0.1, rely=0.1)
    label = tk.Label(frame, text=(f'It cost you: {total_cost} zl'))
    label.place(relx=0.1, rely=0.2)
    label = tk.Label(frame, text=(f'Fuel consumption is: {fuel_consumption} l/100km'))
    label.place(relx=0.1, rely=0.3)
    #label = tk.Label(frame, text=(score))
    #label.place(relx=0.1, rely=0.4)
    label = tk.Label(frame, text=(f'Overall car distance: {car_distance} km'))
    label.place(relx=0.1, rely=0.5)
    button = tk.Button(root, text='Click to continue', command=closing)
    button.pack()
    root.mainloop()


def filling_excel(sheet, wb, name, current_distance, current_price, distance_driven, total_cost, current_liters, fuel_consumption, cost_100km):
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


def displaying_calculated(distance_driven, total_cost, cost_100km, fuel_consumption):
    dist=f"You've driven: {distance_driven} km"
    print(dist)
    trip_cost = f'It cost you: {total_cost} zł'
    print(trip_cost)
    cost_of_100km = f'100 km cost you: {cost_100km} zł'
    print(cost_of_100km)
    liters_per_100km= f'Fuel consumption is: {fuel_consumption} l/100 km'
    print(liters_per_100km)


def displaying_validation_of_style(fuel_consumption):
    if fuel_consumption > 10:
        score = 'Too fast!'
    if fuel_consumption < 10 and fuel_consumption > 5:
        score = 'Fuel consumption is good!'
    if fuel_consumption < 5:
        score = 'Wow, very low !'
    print(score)
