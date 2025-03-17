import tkinter as tk
from tkinter import ttk
import re
import random
import string

# Function to check password strength and return strength level
def check_password_strength(password):
    strength_level = 0
    
    if len(password) >= 8:
        strength_level += 1
    if re.search(r"[A-Z]", password):
        strength_level += 1
    if re.search(r"[a-z]", password):
        strength_level += 1
    if re.search(r"[0-9]", password):
        strength_level += 1
    if re.search(r"[\W_]", password):
        strength_level += 1

    return strength_level

# Function to suggest a strong password
def suggest_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(12))

# Function to handle password check and display strength
def check_password():
    password = entry.get()
    strength = check_password_strength(password)
    
    # Password strength categorization
    if strength == 5:
        result_label.config(text="Strong Password!", fg="green")
    elif strength == 3 or strength == 4:
        result_label.config(text="Moderate Password", fg="orange")
    else:
        result_label.config(text="Weak Password!", fg="red")
        suggested_password = suggest_strong_password()
        suggestion_label.config(text=f"Suggested Strong Password: {suggested_password}", fg="blue")
        copy_button.config(state="normal")
    strength_label.config(text=f"Password Strength: {strength}/5")

# Function to clear password
def clear_password():
    entry.delete(0, tk.END)
    result_label.config(text="")
    suggestion_label.config(text="")
    strength_label.config(text="")
    copy_button.config(state="disabled")

# Function to toggle password visibility
def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(text="Hide Password")
    else:
        entry.config(show='*')
        toggle_button.config(text="Show Password")

# Function to copy the suggested password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(suggestion_label.cget("text").replace("Suggested Strong Password: ", ""))
    root.update()  # Keep clipboard data

# Function to animate button hover (color change)
def on_enter(e):
    e.widget['background'] = '#00BFFF'  # Light blue on hover

def on_leave(e):
    e.widget['background'] = '#007FFF'  # Original blue

# Create the main window
root = tk.Tk()
root.title("Enhanced Password Strength Checker")
root.geometry("450x450")

# Create an input label
input_label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
input_label.pack(pady=10)

# Create an entry widget for password input
entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack(pady=10)

# Create a button to check password strength
check_button = tk.Button(root, text="Check Password", font=("Arial", 12), command=check_password, bg='#007FFF', fg='white', activebackground='#00BFFF', width=15, height=2)
check_button.pack(pady=10)

# Bind hover animations to buttons
check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)

# Create a button to toggle password visibility
toggle_button = tk.Button(root, text="Show Password", font=("Arial", 12), command=toggle_password, bg='#007FFF', fg='white', activebackground='#00BFFF', width=15, height=2)
toggle_button.pack(pady=5)

# Bind hover animations to toggle button
toggle_button.bind("<Enter>", on_enter)
toggle_button.bind("<Leave>", on_leave)

# Label to display password strength result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Label to show password strength in numbers
strength_label = tk.Label(root, text="", font=("Arial", 12))
strength_label.pack(pady=5)

# Label to display password suggestion
suggestion_label = tk.Label(root, text="", font=("Arial", 10), wraplength=400)
suggestion_label.pack(pady=5)

# Create a button to copy suggested password
copy_button = tk.Button(root, text="Copy Password", font=("Arial", 12), command=copy_to_clipboard, bg='#007FFF', fg='white', activebackground='#00BFFF', width=15, height=2, state="disabled")
copy_button.pack(pady=5)

# Bind hover animations to copy button
copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)

# Create a button to clear the password entry
clear_button = tk.Button(root, text="Clear Password", font=("Arial", 12), command=clear_password, bg='#007FFF', fg='white', activebackground='#00BFFF', width=15, height=2)
clear_button.pack(pady=10)

# Bind hover animations to clear button
clear_button.bind("<Enter>", on_enter)
clear_button.bind("<Leave>", on_leave)

# Start the Tkinter event loop
root.mainloop()

