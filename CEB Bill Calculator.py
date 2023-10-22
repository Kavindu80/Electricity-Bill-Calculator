import tkinter as tk


def calculate_bill():
    units = int(entry_units.get())

    if 0 <= units <= 30:
        unit_price = 12
        fixed_price = 180
        total_cost = units * unit_price + fixed_price
    elif 31 <= units <= 60:
        unit_price = 30
        fixed_price = 360
        total_cost = (30 * 12 + (units - 30) * unit_price) + fixed_price
    elif 61 <= units <= 90:
        unit_price = 41
        fixed_price = 480
        total_cost = (30 * 12 + 30 * 30 + (units - 60) * unit_price) + fixed_price
    elif 91 <= units <= 120:
        unit_price = 59
        fixed_price = 1180
        total_cost = (30 * 12 + 30 * 30 + 30 * 41 + (units - 90) * unit_price) + fixed_price
    elif 121 <= units <= 180:
        unit_price = 59
        fixed_price = 1770
        total_cost = (30 * 12 + 30 * 30 + 30 * 41 + 30 * 59 + (units - 120) * unit_price) + fixed_price
    elif 181 <= units:
        unit_price = 89
        fixed_price = 2360
        total_cost = (30 * 12 + 30 * 30 + 30 * 41 + 30 * 59 + 30 * 59 + (units - 180) * unit_price) + fixed_price
    else:
        total_cost = "Invalid input"

    result_label.config(text=f"Total Cost: {total_cost} LKR")



window = tk.Tk()
window.title("Electricity Bill Calculator")


label_units = tk.Label(window, text="Enter the number of units:")
label_units.pack()
entry_units = tk.Entry(window)
entry_units.pack()


calculate_button = tk.Button(window, text="Calculate", command=calculate_bill)
calculate_button.pack()


result_label = tk.Label(window, text="")
result_label.pack()


window.mainloop()
