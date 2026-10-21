import tkinter as tk
from tkinter import messagebox
import math

def calculate_area():
    try:
        # Get value from Entry widget and convert to float
        radius = float(entry_radius.get())
        
        if radius < 0:
            messagebox.showerror("Invalid Input", "Radius cannot be negative.")
            return
        
        # Calculate area of the circle: Area = pi * r^2
        area = math.pi * (radius ** 2)
        
        # Display result in the Label widget
        result_label.config(text=f"Area of the Circle: {area:.2f} sq units")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value for the radius.")

# Create the main window
root = tk.Tk()
root.title("Area of Circle Calculator")
root.geometry("350x230")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="⭕ Area of a Circle", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

# Radius Input
tk.Label(frame, text="Enter Radius:", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
entry_radius = tk.Entry(frame, font=("Arial", 11), width=15)
entry_radius.grid(row=0, column=1, padx=5, pady=5)

# Calculate Area Button
calc_button = tk.Button(root, text="Calculate Area", font=("Arial", 11, "bold"), bg="#FF9800", fg="white", width=15, command=calculate_area)
calc_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Area of the Circle: ", font=("Arial", 11, "bold"), bg="#f0f0f0", fg="#333333")
result_label.pack(pady=10)

# Run the application
root.mainloop()