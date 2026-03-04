import json
import time

class Vehicle:
    def __init__(self, name, price, color_options, category):
        self.name = name
        self.price = price
        self.color_options = color_options
        self.category = category
        self.color = None

    def __str__(self):
        color = f" ({self.color})" if self.color else ""
        return f"{self.name}{color} - ${self.price:,} [{self.category}]"

class Garage:
    def __init__(self, name, capacity):
        self.name = name
        self.vehicles = []
        self.capacity = capacity

    def store_vehicle(self, vehicle):
        if len(self.vehicles) < self.capacity:
            self.vehicles.append(vehicle)
            print(f"{vehicle.name} delivered to {self.name}")
        else:
            print(f"{self.name} is full!")

    def to_dict(self):
        return {
            "name": self.name,
            "capacity": self.capacity,
            "vehicles": [vars(v) for v in self.vehicles]
        }

    def load_from_dict(self, data):
        self.vehicles = []
        for v_data in data["vehicles"]:
            # Create a new Vehicle object without the 'color' attribute initially
            vehicle = Vehicle(name=v_data['name'], price=v_data['price'], color_options=v_data['color_options'], category=v_data['category'])
            # Assign the color attribute separately if it exists in the loaded data
            if 'color' in v_data:
                vehicle.color = v_data['color']
            self.vehicles.append(vehicle)


class Berth(Garage):
    pass


class Website:
    def __init__(self, name, vehicle_list):
        self.name = name
        self.vehicle_list = vehicle_list

    def list_vehicles(self):
        for i, v in enumerate(self.vehicle_list):
            print(f"{i}: {v}")

    def get_vehicle(self, index):
        return self.vehicle_list[index] if 0 <= index < len(self.vehicle_list) else None


class Player:
    def __init__(self, money):
        self.money = money
        self.garage = Garage("Los Santos Garage", 6)
        self.berth = Berth("Vespucci Berth", 3)

    def buy_vehicle(self, vehicle):
        if self.money >= vehicle.price:
            print("Choose color:")
            for i, color in enumerate(vehicle.color_options):
                print(f"{i}: {color}")
            color_idx = input("> ")
            if color_idx.isdigit() and 0 <= int(color_idx) < len(vehicle.color_options):
                vehicle.color = vehicle.color_options[int(color_idx)]
                print("Processing delivery...")
                time.sleep(1)  # simulate delivery delay
                if vehicle.category == "Boat":
                    self.berth.store_vehicle(vehicle)
                else:
                    self.garage.store_vehicle(vehicle)
                self.money -= vehicle.price
                print(f"${vehicle.price:,} deducted. New balance: ${self.money:,}")
            else:
                print("Invalid color.")
        else:
            print("Insufficient funds.")

    def save(self):
        data = {
            "money": self.money,
            "garage": self.garage.to_dict(),
            "berth": self.berth.to_dict()
        }
        with open("savefile.json", "w") as f:
            json.dump(data, f, indent=2)
        print("Game saved.")

    def load(self):
        try:
            with open("savefile.json", "r") as f:
                data = json.load(f)
                self.money = data["money"]
                self.garage.load_from_dict(data["garage"])
                self.berth.load_from_dict(data["berth"])
            print("Game loaded.")
        except FileNotFoundError:
            print("No save file found.")

    def list_owned_vehicles(self):
        all_vehicles = self.garage.vehicles + self.berth.vehicles
        if not all_vehicles:
            print("You don't own any vehicles yet.")
            return None
        print("\n--- YOUR VEHICLES ---")
        for i, vehicle in enumerate(all_vehicles):
            print(vehicle)
        return all_vehicles


# Vehicle database
super_cars = [
    Vehicle("Adder", 1000000, ["Red", "Black", "White", "Blue"], "Super"),
    Vehicle("Entity XF", 795000, ["Blue", "Silver", "Black"], "Super"),
]
boats = [
    Vehicle("Speeder", 325000, ["Red", "White", "Blue"], "Boat"),
    Vehicle("Dinghy", 125000, ["Green", "Gray", "Black"], "Boat"),
]
motorcycles = [
    Vehicle("Bati 801", 10000, ["Red", "White", "Black", "Blue"], "Motorcycle"),
    Vehicle("PCJ 600", 9000, ["White", "Black", "Red"], "Motorcycle"),
    Vehicle("Faggio", 900, ["Black", "White", "Red", "Yellow"], "Motorcycle")
]
aircraft = [
    Vehicle("Luxor", 1625000, ["White", "Gold", "Black"], "Aircraft"),
    Vehicle("Frogger", 1300000, ["Silver", "Black", "Red"], "Aircraft"),
]
cycles = [
    Vehicle("Racing Bike", 2500, ["White"], "Bicycle"),
    Vehicle("BMX", 500, ["Gray"], "Bicycle"),
    Vehicle("Scorcher", 1000, ["Gray"], "Bicycle"),
    Vehicle("Cruiser", 3000, ["White", "Vintage Brown"], "Bicycle")
]

# Websites
websites = {
    "1": Website("Legendary Motorsport", super_cars),
    "2": Website("Dock Tease", boats),
    "3": Website("Southern S.A. Super Autos", motorcycles),
    "4": Website("Elitas Travel", aircraft),
    "5": Website("Pedal And Metal", cycles)
}

def display_homepage():
    print("\n--- VEHICLE WEBSITES ---")
    for k, site in websites.items():
        print(f"{k}: {site.name}")
    print("owned: View owned vehicles")
    print("save: Save game")
    print("load: Load game")
    print("exit: Exit game")


def shop_website(player, site: Website):
    while True:
        print(f"\n--- {site.name} ---")
        site.list_vehicles()
        print("Type index to buy, or 'back' to return.")
        choice = input("> ").strip().lower()

        if choice == "back":
            return
        elif choice.isdigit():
            idx = int(choice)
            vehicle = site.get_vehicle(idx)
            if vehicle:
                print(f"Buy {vehicle.name} for ${vehicle.price:,}? [y/n]")
                confirm = input("> ").strip().lower()
                if confirm == "y":
                    player.buy_vehicle(vehicle)
                else:
                    print("Purchase cancelled.")
            else:
                print("Invalid vehicle index.")
        else:
            print("Invalid input.")


# Game loop
player = Player(money=15000000)

while True:
    display_homepage()
    print(f"Current balance: ${player.money:,}")
    choice = input("> ").strip().lower()

    if choice == "exit":
        break
    elif choice == "save":
        player.save()
    elif choice == "load":
        player.load()
    elif choice == "owned":
        owned_vehicles = player.list_owned_vehicles()
    elif choice in websites:
        shop_website(player, websites[choice])
    else:
        print("Invalid choice.")