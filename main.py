"""
Quang Huynh
something fun because bored

11/20/24
"""


import tkinter as tk
from tkinter import messagebox

def scan_database():
    card_number = card_number_entry.get()
    expiration_date = expiration_date_entry.get()
    cvv = cvv_entry.get()
    zip_code = zip_code_entry.get()

    if not card_number or not expiration_date or not cvv or not zip_code:
        messagebox.showerror("Error", "All fields are required!")
        return

    # simulate scanning databases
    scanning_label.config(text="Scanning databases...")
    root.update_idletasks()  # Update the GUI
    # simulated scanning delay
    import time
    time.sleep(2)

    scanning_label.config(text="Success!")
    messagebox.showinfo("Result", "Your card number did not show up in any of the hacker's databases.")

# create the main window
root = tk.Tk()
root.title("Credit Card Security Check")

# GUI layout
tk.Label(root, text="Is your credit card number in a hacker's database?", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="You can easily find out now! Enter your information below:", font=("Arial", 10)).pack()

tk.Label(root, text="Credit Card Number:").pack()
card_number_entry = tk.Entry(root, width=30)
card_number_entry.pack()

tk.Label(root, text="Expiration Date (MM/YY):").pack()
expiration_date_entry = tk.Entry(root, width=30)
expiration_date_entry.pack()

tk.Label(root, text="CVV:").pack()
cvv_entry = tk.Entry(root, width=30, show="*")  # hides input with asterisks for security
cvv_entry.pack()

tk.Label(root, text="Your Zip Code:").pack()
zip_code_entry = tk.Entry(root, width=30)
zip_code_entry.pack()

scan_button = tk.Button(root, text="SCAN DATABASE", command=scan_database, bg="orange", fg="white", font=("Arial", 12))
scan_button.pack(pady=10)

scanning_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
scanning_label.pack(pady=5)

# run the GUI loop
root.mainloop()
