import tkinter as tk
import requests

def get_bitcoin_price(currency):
    try:
        # Fetch the Bitcoin price in the selected currency from CoinGecko API
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={currency}")
        data = response.json()
        price = data['bitcoin'][currency]
        return price
    except Exception as e:
        # If there's an error, return the error message
        return f"Error: {str(e)}"

def update_price():
    currency = currency_var.get()  # Get selected currency from dropdown
    price = get_bitcoin_price(currency)
    price_label.config(text=f"Current Bitcoin Price: {price} {currency.upper()}")
    # Call this function again after 60 seconds (60000 milliseconds)
    root.after(60000, update_price)

def currency_changed(*args):
    update_price()  # Update price when currency is changed

# Setting up the tkinter window
root = tk.Tk()
root.title("Real-Time Bitcoin Price")
root.geometry("350x150")

# Create a label to display the Bitcoin price
price_label = tk.Label(root, text="Current Bitcoin Price: Loading...", font=('Helvetica', 16))
price_label.pack(pady=20)

# Currency options
currency_options = ['usd', 'eur', 'gbp', 'jpy', 'aud']
currency_var = tk.StringVar(value='usd')  # Set default currency

# Create a dropdown menu for selecting currency
currency_menu = tk.OptionMenu(root, currency_var, *currency_options, command=currency_changed)
currency_menu.pack(pady=10)

# Start the price update process
update_price()

# Start the tkinter main loop
root.mainloop()