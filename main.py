import data
import cities
import passangers
import economy
import settings
from station import stations_menu
from route import routes_menu
from trains import trains_menu, move_train
import random


def is_input_validation(inp) -> bool:
    for c in inp:
        if c.isdigit() or c.isalpha():
            continue
        else:
            return False
    return True


def main_menu_input_handler(inp, moneySave):
    inp = inp.lower()
    if not is_input_validation(inp):
        main_menu_input_handler(
            input("please dont use any spaces or special charcters\n")
        )
    match inp:
        case "q" | "Q":
            print("quiting\n")
            return "q"
        case "":
            pass
        case "0" | "help":
            print_help()
        case "1" | "city":
            cities.cities_menu(cityData)
        case "2" | "station":
            stations_menu(stationData, cityData)
        case "3" | "train":
            # ToDo: set new trainData in the function itself. not here
            global trainData
            trainData = trains_menu(trainData, routeData, money)
        case "4" | "route":
            routes_menu(routeData, stationData, trainData)
        case "S" | "s" | "save" | "SAVE":
            print(moneySave)
            data.write_save_data(
                cityData,
                stationData,
                routeData,
                trainData,
                days,
                moneySave,
                gameSettings,
                saveName,
            )
        case _:
            inp = main_menu_input_handler(input("please pick on of our options\n"))


def menu_handler(loaded_data):
    while True:
        print_main_menu()
        user_input = input("input? \n")
        match user_input:
            case "0":
                return print_save_menu(loaded_data)
                break
            case "1":
                return new_save()
            case "q" | "Q":
                exit()
            case _:
                pass


def print_help():
    print("This is the list of all commands")
    print("-" * 67)
    print(f"|{'index':>7} | {"command":>12} | {"description":>40}|")
    print("-" * 67)
    print(f"|{'0':>7} | {"Help":>12} | {"Lists all commands":>40}|")
    print(f"|{'1':>7} | {"Cities":>12} | {"Opens the cities menu":>40}|")
    print(f"|{'2':>7} | {"Stations":>12} | {"Opens the stations menu":>40}|")
    print(f"|{'3':>7} | {"Trains":>12} | {"Opens the routes menu":>40}|")
    print(f"|{'4':>7} | {"Routes":>12} | {"Opens the trains menu":>40}|")
    print(f"|{'s':>7} | {"Save":>12} | {"Saves the current state of the game":>40}|")
    print(f"|{'q':>7} | {"Quit":>12} | {"Quits the game or the current menu":>40}|")
    print("-" * 67)
    return main_menu_input_handler(input("pick a input"))


def print_main_menu():
    print("main menu")
    print("-" * 24)
    print(f"|{'0':>7} | {"load game":>12}|")
    print(f"|{'1':>7} | {"new game":>12}|")
    print(f"|{'q':>7} | {"quite":>12}|")
    print("-" * 24)


def print_save_menu(all_saves):
    while True:
        for save in all_saves:
            print(save, all_saves[save]["name"])
        user_input = input("select save: ")
        if user_input in all_saves:
            print("game start")
            return all_saves[user_input]
        elif user_input == "q" or user_input == "Q":
            break
        else:
            print("please select a save file by index")


def main_game_loop(days, money, cityData, stationData, trainData, routeData, saveName):
    while money > -10000:
        days += 1
        # Show where each train is if there are trains
        if len(trainData) > 0:
            for train in trainData.values():
                percentage = train["metersOnRoute"]
                route = routeData[str(train["currentRouteId"])]
                num_segments = 50  # Number of track spaces
                train_pos = int((percentage / 100) * num_segments)

                progress = "X"
                for i in range(1, num_segments + 1):
                    if i == train_pos:
                        progress += "T"
                    else:
                        progress += "-"
                progress += "X"

                print(f"Train {train["name"]}: {progress}")
        menu = main_menu_input_handler(
            input(
                f"""
    money: {money} | trains: {len(trainData)} | stations: {len(stationData)} | routes: {len(routeData)} | cities: {len(cityData)} | day: {days}
    new action:
    """
            ),
            money,
        )
        if menu == "q":
            break

        if random.randint(0, 500) == 1:
            cityData = cities.new_city(cityData)

        if random.randint(0, 20) == 1:
            # ToDo: add some logic to this so cities dont actually randomly grow. Let them grow on a condition.
            cityData = cities.grow_city(cityData)

        oldMoney = money
        trainData, money = move_train(trainData, money, stationData, routeData)

        stationData = passangers.spawn_passangers(cityData, stationData)

        maintenance = economy.maintenance(stationData, trainData, routeData)
        money -= maintenance
        profit = money - oldMoney
        print(f"Your maintenance cost today was {maintenance}")
        print(f"Your profit today was {profit}")


def new_save(): 
    save_name = input("give your save a name: ")
    setting = settings.settings_menu()
    print("making cities")
    city = {}
    city = cities.new_city(city)
    city = cities.new_city(city)
    return data.in_memory_save(save_name, setting, city)


def main():
    global cityData
    global stationData
    global trainData
    global routeData
    global money
    global saveName
    global days
    global gameSettings
    loaded_data = data.load_game_data()
    loaded_save_data = {}
    while True:
        loaded_save_data = menu_handler(loaded_data)
        if not loaded_save_data:
            pass
        else:
            saveName = loaded_save_data["name"]
            days = loaded_save_data["days"]
            money = loaded_save_data["money"]
            cityData = loaded_save_data["cities"]
            stationData = loaded_save_data["stations"]
            trainData = loaded_save_data["trains"]
            routeData = loaded_save_data["routes"]
            gameSettings = loaded_save_data["gameSettings"]
            main_game_loop(
                days, money, cityData, stationData, trainData, routeData, saveName
            )
            print("You ran out of money!")
            print("Game Over")


main()
