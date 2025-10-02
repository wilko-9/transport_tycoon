import data
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


def main_menu_input_handler(inp) -> str:
    inp = inp.lower()
    if not is_input_validation(inp):
        main_menu_input_handler(
            input("please dont use any spaces or special charcters\n")
        )
    match inp:
        case "q":
            print("quiting\n")
            return "q"
        case "0" | "help":
            return "help"
        case "1" | "city":
            return "city"
        case "2" | "station":
            stations_menu(data.StationsData())
            return "station"
        case "3" | "train":
            trains_menu(data.trainsData())
            return "train"
        case "4" | "route":
            routes_menu(data.routesData())
            return "route"
        case _:
            inp = main_menu_input_handler(input
                                          ("please pick on of our optiions\n")
                                          )
            return inp


def main():
    while True:
        menu = main_menu_input_handler(input(f"""
money: ??? trains: {len(data.trainsData())} stations: {len(data.StationsData())} routes: {len(data.routesData())}
new action:
"""))
        if menu == "q":
            break


main()
