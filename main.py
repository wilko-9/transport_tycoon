import data
import cities
import passangers
from station import stations_menu
from route import routes_menu
from trains import trains_menu


def is_input_validation(inp) -> bool:
    for c in inp:
        if c.isdigit() or c.isalpha():
            continue
        else:
            return False
    return True

def main_menu_input_handler(inp, city):
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
            return "station"
        case "3" | "train":
            trains_menu(data.trains_data())
        case "4" | "route":
            routes_menu(data.routes_data())
        case _:
            inp = main_menu_input_handler(input
                                          ("please pick on of our optiions\n")
                                          )

def help():
    print("This is the list of all commands")
    print("0 | Help | Lists all commands")
    print("1 | Cities | Opens the cities menu")
    print("2 | Stations | Opens the stations menu")
    print("3 | Routes | Opens the routes menu")
    print("4 | Trains | Opens the trains menu")
    print("Q | Quit | Quits the game or the current menu")

    return main_menu_input_handler(input("pick a input"))

def main():
    global cityData
    global stationData

    days = 0
    money = 5000
    cityData = data.city_data()
    stationData = data.stations_data()
    while money > -10000:
        days += 1
        menu = main_menu_input_handler(input(f"""
money: ??? trains: {len(data.trains_data())} stations: {len(data.stations_data())} routes: {len(data.routes_data())}
new action:
"""), cityData)
        if menu == "q":
            break

        if range(0, 51) == 1:
            cityData = cities.new_city(cityData)
        
        stationData = passangers.spawn_passangers(cityData, stationData)
        # print(stationData)
    
    print("You ran out of money!")
    print("Game Over")

main()
