import tkinter as tk
from tkinter import messagebox
import requests
from PIL import ImageTk, Image

def convert_currency():
    amount_str = entry_amount.get()

    # Validation
    if not amount_str:
        messagebox.showerror("Error", "Amount not entered.\nPlease enter a valid amount.")
        return

    try:
        amount = float(amount_str)
    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only.")
        return

    from_currency = from_var.get()
    to_currency = to_var.get()

    if from_currency == "CURRENCY" or to_currency == "CURRENCY":
        messagebox.showerror("Error", "Please select both currencies.")
        return

    try:
        # Fetch exchange rate
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        exchange_rate = data["rates"][to_currency]
        converted_amount = amount * exchange_rate

        result_label.config(
            text=f"{amount} {from_currency} = {converted_amount:.4f} {to_currency}"
        )

    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch exchange rates.\nCheck your internet connection.")

# ------------------- GUI -------------------

window = tk.Tk()
window.title("Currency Converter")
window.geometry("700x400")
window.resizable(False, False)

# Background Image
background_image = Image.open("C:\\Users\\DELL\\Desktop\\img.jpg")
resized_bg_image = background_image.resize((700, 400))
background_photo = ImageTk.PhotoImage(resized_bg_image)

canvas = tk.Canvas(window, width=700, height=400)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Heading
label_head = tk.Label(
    window,
    font=('Times New Roman', 25, 'bold'),
    text="-- CURRENCY CONVERTER --",
    bg="#0077b6",
    fg="black"
)
label_head.place(x=140, y=30)

# Amount
label_amount = tk.Label(
    window,
    font=('Times New Roman', 20, 'bold'),
    text="Enter Amount:",
    bg="#00b4d8",
    fg="black"
)
label_amount.place(x=50, y=100)

entry_amount = tk.Entry(window, font=('Times New Roman', 14))
entry_amount.place(x=400, y=100, height=30)

# From Currency
label_from_currency = tk.Label(
    window,
    font=('Times New Roman', 20, 'bold'),
    text="From Currency:",
    bg="#00b4d8",
    fg="black"
)
label_from_currency.place(x=50, y=150)

# To Currency
label_to_currency = tk.Label(
    window,
    font=('Times New Roman', 20, 'bold'),
    text="To Currency:",
    bg="#00b4d8",
    fg="black"
)
label_to_currency.place(x=50, y=200)

from_var = tk.StringVar(window)
from_var.set("CURRENCY")

to_var = tk.StringVar(window)
to_var.set("CURRENCY")

currencies = ['USD', 'EUR', 'GBP', 'INR', 'CAD']

from_menu = tk.OptionMenu(window, from_var, *currencies)
from_menu.place(x=400, y=150)

to_menu = tk.OptionMenu(window, to_var, *currencies)
to_menu.place(x=400, y=200)

# Convert Button
convert_button = tk.Button(
    window,
    font=('Times New Roman', 15, 'bold'),
    text="CONVERT",
    bg="#57A0D3",
    fg="black",
    command=convert_currency
)
convert_button.place(x=300, y=250)

# Result
label_result = tk.Label(
    window,
    font=('Times New Roman', 20, 'bold'),
    text="Converted Amount:",
    bg="#00b4d8",
    fg="black"
)
label_result.place(x=50, y=330)

result_label = tk.Label(
    window,
    font=('Times New Roman', 14),
    text="",
    bg="white",
    width=25
)
result_label.place(x=400, y=330, height=30)

window.mainloop()
