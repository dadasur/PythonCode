import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    
    # Predefined credentials for validation
    correct_user = "admin"
    correct_pass = "password123"
    
    if not username or not password:
        messagebox.showwarning("Input Error", "Please fill in both fields.")
        return

    # Check credentials
    if username == correct_user and password == correct_pass:
        result_label.config(
            text="✅ Login Successful! Welcome, admin.", 
            fg="#2e7d32"
        )
    else:
        result_label.config(
            text="❌ Invalid Username or Password.", 
            fg="#c62828"
        )

# Create the main window
root = tk.Tk()
root.title("Basic Login Form")
root.geometry("360x280")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="🔐 User Login", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

# Username Input
tk.Label(frame, text="Username:", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
entry_username = tk.Entry(frame, font=("Arial", 11), width=18)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Password Input (masked with '*')
tk.Label(frame, text="Password:", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
entry_password = tk.Entry(frame, font=("Arial", 11), width=18, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Login Button
login_button = tk.Button(
    root, 
    text="Login", 
    font=("Arial", 11, "bold"), 
    bg="#008CBA", 
    fg="white", 
    width=14, 
    command=validate_login
)
login_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 10, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

# Run the application
root.mainloop()