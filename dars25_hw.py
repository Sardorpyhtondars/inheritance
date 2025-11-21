class Products:
    def __init__(self, date, price, size):
        self.date = date
        self.price = price
        self.size = size

    def __str__(self):
        return f"Date: {self.date}, Price: {self.price}, Size: {self.size}"

class TV(Products):
    def __init__(self, date, price, size, channels, smart):
        super().__init__(date, price, size)
        self.channels = channels
        self.smart = smart

    def __str__(self):
        return f"{super().__str__()}, Channels: {self.channels}, Smart: {self.smart}"

class Headphone(Products):
    def __init__(self, date, price, size, weight, wireless):
        super().__init__(date, price, size)
        self.weight = weight
        self.wireless = wireless

    def __str__(self):
        return f"{super().__str__()}, Weight: {self.weight}, Wireless: {self.wireless}"

class Fridge(Products):
    def __init__(self, date, price, size, volume, doors):
        super().__init__(date, price, size)
        self.volume = volume
        self.doors = doors

    def __str__(self):
        return f"{super().__str__()}, Volume: {self.volume}, Doors: {self.doors}"

class Shop:
    def __init__(self, place, shop_type):
        self.place = place
        self.shop_type = shop_type

    def manager(self):
        while True:
            kod = input(" 1. View TV\n 2. View Headphone\n 3. View Fridge\n 4. Exit\n")
            if kod == "1":
                print(tv)
            elif kod == "2":
                print(headphone)
            elif kod == "3":
                print(fridge)
            elif kod == "4":
                break
            else:
                print("Invalid input")
                continue

tv=TV("2024", "10000000", "0.70x0.50", "70 channels", "smart TV")
headphone=Headphone("2021", "250000", "0.05x0.07", "50 gramms", "Wireless")
fridge=Fridge("2025", "7000000", "2x1x1", "20 m³", "4 doors")

shop=Shop("Xadra", "Electronics")
shop.manager()
