import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        # Get values from Entry widgets and convert to float
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Calculate addition
        result = num1 + num2
        
        # Display result in the Label widget
        result_label.config(text=f"Result: {num1} + {num2} = {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Addition of Two Numbers")
root.geometry("350x250")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Addition App", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

# First Number Input
tk.Label(frame, text="First Number:", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
entry1 = tk.Entry(frame, font=("Arial", 11), width=15)
entry1.grid(row=0, column=1, padx=5, pady=5)

# Second Number Input
tk.Label(frame, text="Second Number:", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
entry2 = tk.Entry(frame, font=("Arial", 11), width=15)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Add Button
add_button = tk.Button(root, text="Add", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=10, command=add_numbers)
add_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333333")
result_label.pack(pady=10)

# Run the application
root.mainloop()