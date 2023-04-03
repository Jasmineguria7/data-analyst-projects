import tkinter as tk
import requests  # requests is a popular third-party Python library that provides a simple and elegant way to send HTTP requests using Python.

class CryptoApp(tk.Frame): #you'll be able to access all the methods and properties defined in the class.
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Crypto App")
        self.pack(fill=tk.BOTH, expand=True)

        self.search_label = tk.Label(self, text="Search Cryptocurrency:")
        self.search_label.pack(pady=10)

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.search_button = tk.Button(self, text="Search", command=self.search_crypto)
        self.search_button.pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def search_crypto(self):
        crypto = self.search_entry.get()
        url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={crypto}"
        response = requests.get(url).json()
        if response:
            name = response[0]["name"]
            price = response[0]["current_price"]
            market_cap = response[0]["market_cap"]
            self.result_label.configure(text=f"{name}\nPrice: ${price}\nMarket Cap: ${market_cap}")
        else:
            self.result_label.configure(text="Cryptocurrency not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
root.mainloop()
    