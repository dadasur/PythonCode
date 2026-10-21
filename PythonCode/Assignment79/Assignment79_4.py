import tkinter as tk
from tkinter import messagebox

def check_eligibility():
    name = entry_name.get().strip()
    age_text = entry_age.get().strip()
    
    if not name:
        messagebox.showwarning("Input Error", "Please enter the person's name.")
        return

    try:
        age = int(age_text)
        
        if age < 0:
            messagebox.showerror("Invalid Input", "Age cannot be negative.")
            return

        # Check eligibility
        if age >= 18:
            result_label.config(
                text=f"✅ {name} is ELIGIBLE to vote!", 
                fg="#2e7d32"
            )
        else:
            years_left = 18 - age
            result_label.config(
                text=f"❌ {name} is NOT ELIGIBLE to vote.\n(Eligible in {years_left} year{'s' if years_left > 1 else ''})", 
                fg="#c62828"
            )
            
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid whole number for age.")

# Create the main window
root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("380x270")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="🗳️ Voting Eligibility Checker", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

# Name Input
tk.Label(frame, text="Name:", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(frame, font=("Arial", 11), width=18)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Age Input
tk.Label(frame, text="Age:", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
entry_age = tk.Entry(frame, font=("Arial", 11), width=18)
entry_age.grid(row=1, column=1, padx=5, pady=5)

# Check Eligibility Button
check_button = tk.Button(
    root, 
    text="Check Eligibility", 
    font=("Arial", 11, "bold"), 
    bg="#673AB7", 
    fg="white", 
    width=16, 
    command=check_eligibility
)
check_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 11, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

# Run the application
root.mainloop()