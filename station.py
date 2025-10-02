def stations_menu(stations):
    print("stations")
    for station in stations.values():
        print(f"""{station["name"]} \t | {station["waitingPassangers"]} \t |  {station["amountOfRoutes"]} """)
    print("Type 'q' to go back| 1 or 'add' add | 2 or 'edit' to edit  | 3 or 'delete' to delete")

    inp = input()

    match inp:
        case "q":
            pass
        case "1" | "add":
            add_station()
        case "2" | "edit":
            edit_station()
        case "3" | "delete":
            delete_station()
        case _:
            stations_menu(stations)


def add_station():
    print("station has been added")


def edit_station():
    print("station has been edited")


def delete_station():
    print("station has been deleted")
