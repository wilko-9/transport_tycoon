import data
import cities
import passangers
import economy
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


def main_menu_input_handler(inp):
    inp = inp.lower()
    if not is_input_validation(inp):
        main_menu_input_handler(
            input("please dont use any spaces or special charcters\n")
        )
    match inp:
        case "q":
            print("quiting\n")
            return "q"
        case "":
            pass
        case "0" | "help":
            help()
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
        case _:
            inp = main_menu_input_handler(input
                                          ("please pick on of our options\n")
                                          )


def help():
    print("This is the list of all commands")
    print("-" * 67)
    print(f"|{'index':>7} | {"command":>12} | {"description":>40}|")
    print("-" * 67)
    print(f"|{'0':>7} | {"Help":>12} | {"Lists all commands":>40}|")
    print(f"|{'1':>7} | {"Cities":>12} | {"Opens the cities menu":>40}|")
    print(f"|{'2':>7} | {"Stations":>12} | {"Opens the stations menu":>40}|")
    print(f"|{'3':>7} | {"Trains":>12} | {"Opens the routes menu":>40}|")
    print(f"|{'4':>7} | {"Routes":>12} | {"Opens the trains menu":>40}|")
    print(f"|{'q':>7} | {"Quit":>12} | {"Quits the game or the current menu":>40}|")
    print("-" * 67)
    return main_menu_input_handler(input("pick a input"))


def main():
    global cityData
    global stationData
    global trainData
    global routeData
    global money

    days = 0
    money = 50000
    cityData = data.city_data()
    stationData = data.stations_data()
    trainData = data.trains_data()
    routeData = data.routes_data()
    while money > -10000:
        days += 1 #to use in menu for time tracking
        menu = main_menu_input_handler(input(f"""
money: {money} | trains: {len(trainData)} | stations: {len(stationData)} | routes: {len(routeData)}
new action:
"""))
        if menu == "q":
            break

        if random.randint(0,50) == 1:
            cityData = cities.new_city(cityData)
        
        if random.randint(0,50) == 1:
            cityData = cities.grow_city(cityData)

        trainData, money = move_train(trainData, money, stationData, routeData)

        stationData = passangers.spawn_passangers(cityData, stationData)
        
        maintenance = economy.maintenance(stationData, trainData, routeData)
        money -= maintenance
        print(f"Your maintenance cost today was {maintenance}")

    print("You ran out of money!")
    print("Game Over")



main() 
