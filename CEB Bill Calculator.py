import tkinter as tk

# Function to calculate the electricity bill
def calculate_bill():
    units = int(entry_units.get())

 # Define electricity rates and fixed charges for different unit ranges
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


# Create the main window
window = tk.Tk()
window.title("Electricity Bill Calculator")

# Label and Entry for user to input the number of units
label_units = tk.Label(window, text="Enter the number of units:")
label_units.pack()
entry_units = tk.Entry(window)
entry_units.pack()

# Button to trigger the bill calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate_bill)
calculate_button.pack()

# Label to display the calculated total cost
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
