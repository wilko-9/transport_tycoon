from data import StationsData


def is_input_validation(inp) -> bool:
    for c in inp:
        if c.isdigit() or c.isalpha():
            continue
        else:
            return False
    return True


def stations_menu(stations):
    print("stations")
    for station in stations.values():
        print(f"""{station["name"]} \t | {station["expectedPeople"]} \t |  {station["amountOfRoutes"]} """)
    print("Type 'q' to go back| 1 or \"add\" add | 2 or \"edit\" to edit  | 3 or \"delete\" to delete")


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
            stations_menu(StationsData())
            return "station"
        case "3" | "train":
            return "train"
        case "4" | "route":
            return "route"
        case _:
            inp = main_menu_input_handler(input
                                          ("please pick on of our optiions\n")
                                          )
            return inp


def main():
    while True:
        menu = main_menu_input_handler(input("pick a input\n"))
        if menu == "q":
            break


main()
