import tkinter as tk
from tkinter import messagebox

def find_maximum():
    try:
        # Get values from Entry widgets and convert to float
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        
        # Find the maximum number
        max_num = max(num1, num2, num3)
        
        # Display result in the Label widget
        result_label.config(text=f"The Largest Number is: {max_num}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values in all fields.")

# Create the main window
root = tk.Tk()
root.title("Find Maximum Number")
root.geometry("360x300")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="📈 Find the Largest Number", font=("Arial", 14, "bold"), bg="#f0f0f0")
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

# Third Number Input
tk.Label(frame, text="Third Number:", font=("Arial", 11), bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
entry3 = tk.Entry(frame, font=("Arial", 11), width=15)
entry3.grid(row=2, column=1, padx=5, pady=5)

# Find Maximum Button
max_button = tk.Button(root, text="Find Maximum", font=("Arial", 11, "bold"), bg="#2196F3", fg="white", width=15, command=find_maximum)
max_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="The Largest Number is: ", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333333")
result_label.pack(pady=10)

# Run the application
root.mainloop()