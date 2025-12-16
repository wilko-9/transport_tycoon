import random
import os
import pickle
import settings
from station import stations_menu
from route import routes_menu
from trains import trains_menu, move_trains
from cities import City, city_logic
from economy import maintenance

SAVE_FOLDER = "saves"


# Save / Load Functions

def save_game(save_name, days, money, city_list, station_list, train_list, route_list, settings_data):
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)
    file_path = os.path.join(SAVE_FOLDER, f"{save_name}.pkl")
    with open(file_path, "wb") as f:
        pickle.dump({
            "days": days,
            "money": money,
            "cities": city_list,
            "stations": station_list,
            "trains": train_list,
            "routes": route_list,
            "settings": settings_data
        }, f)
    print(f"Game saved as '{save_name}'.")


def load_saves():
    if not os.path.exists(SAVE_FOLDER):
        return {}
    saves = {}
    for file in os.listdir(SAVE_FOLDER):
        if file.endswith(".pkl"):
            save_name = file.replace(".pkl", "")
            saves[save_name] = file
    return saves


def load_game(save_name):
    file_path = os.path.join(SAVE_FOLDER, f"{save_name}.pkl")
    if not os.path.exists(file_path):
        print("Save not found.")
        return None
    with open(file_path, "rb") as f:
        data = pickle.load(f)
    return data


def load_game_menu():
    saves = load_saves()
    if not saves:
        print("No saves found.")
        return None
    while True:
        print("Available saves:")
        for save_name in saves:
            print(f"- {save_name}")
        choice = input("Select a save name (or 'q' to cancel): ").strip()
        if choice.lower() == "q":
            return None
        if choice in saves:
            return load_game(choice)
        print("Invalid selection.")


# Main Menu Helpers

def is_input_validation(inp) -> bool:
    return all(c.isalnum() for c in inp)


def get_valid_input(prompt, allowed_inputs):  # TODO: use everywhere
    while True:
        user_input = input(prompt).strip()
        if user_input in allowed_inputs:
            return user_input
        else:
            print(f"Invalid input. Please enter one of: {', '.join(allowed_inputs)}")


def print_help():
    print("Commands:")
    print("0: Help | 1: Cities | 2: Stations | 3: Trains | 4: Routes | 5: Next Day | s: Save | q: Quit")


def main_menu_input_handler(inp, city_list, station_list, route_list, train_list, money, days, settings_data):
    inp = inp.lower().strip()
    if not is_input_validation(inp):
        return main_menu_input_handler(
            input("Please don't use spaces or special characters:\n"),
            city_list, station_list, route_list, train_list, money, days, settings_data
        )

    match inp:
        case "q":
            case = get_valid_input("would you like to save and quit? (1) yes (2) no", ["1", "2"])
            if case == "1":
                save_name = input("Enter save name: ").strip()
                save_game(save_name, days, money, city_list, station_list, train_list, route_list, settings_data)
            print("Quitting...")
            return "q", city_list, station_list, route_list, train_list, money, days
        case "0" | "help":
            print_help()
        case "1" | "city":
            from cities import cities_menu
            cities_menu(city_list)
        case "2" | "station":
            money = stations_menu(station_list, city_list, money)
        case "3" | "train":
            money = trains_menu(train_list, route_list, money)
        case "4" | "route":
            routes_menu(route_list, station_list, train_list)
        case "5" | "next day":
            return None, city_list, station_list, route_list, train_list, money, days
        case "s":
            save_name = input("Enter save name: ").strip()
            save_game(save_name, days, money, city_list, station_list, train_list, route_list, settings_data)
        case _:
            print("Invalid input. Returning to menu")

    return main_menu_input_handler(
                input("Pick an option:\n"),
                city_list, station_list, route_list, train_list, money, days, settings_data
            )


# Game Loop

def main_game_loop(city_list, station_list, train_list, route_list, money, days, settings_data):
    while money > -10000:
        days += 1

        # Update cities (growth & spawn passengers)
        city_logic(city_list)

        # Display train progress
        for train in train_list:
            if train.route:
                num_segments = 50
                train_pos = int((train.percentage_route / 100) * num_segments)
                progress = "X" + "".join(
                    ["T" if i == train_pos else "-" for i in range(1, num_segments + 1)]
                ) + "X"
                print(f"Train {train.name}: {progress}")

        # Main menu
        menu, city_list, station_list, route_list, train_list, money, days = main_menu_input_handler(
            input(f"""
Money: {money} | Trains: {len(train_list)} | Stations: {len(station_list)} | Routes: {len(route_list)} | Cities: {len(city_list)} | Day: {days}
New action:
"""),
            city_list, station_list, route_list, train_list, money, days, settings_data
        )
        if menu == "q":
            break

        # Move trains
        money = move_trains(train_list, money)

        # Maintenance
        maintenance_cost = maintenance(station_list, train_list, route_list)
        money -= maintenance_cost
        print(f"Maintenance cost today: {maintenance_cost}")


def start_new_game():
    money = settings.startingMoney
    days = 0
    city_list = [City(0, random.randint(0, 100), random.randint(0, 100)) for _ in range(5)]
    station_list = []
    train_list = []
    route_list = []

    settings_data = {}
    main_game_loop(city_list, station_list, train_list, route_list, money, days, settings_data)


def main():
    print("Welcome to Transport Simulator!")
    choice = input("Start (1) New Game or (2) Load Game? ").strip()
    if choice == "2":
        save_data = load_game_menu()
        if save_data:
            main_game_loop(
                save_data["cities"],
                save_data["stations"],
                save_data["trains"],
                save_data["routes"],
                save_data["money"],
                save_data["days"],
                save_data["settings"]
            )
        else:
            new_choice = input("No save found. Would you like to start a new game instead? (1) Yes or (2) No").strip()
            if new_choice == "1":
                start_new_game()
            else:
                print("Quitting game")
    else:
        start_new_game()


if __name__ == "__main__":
    main()
