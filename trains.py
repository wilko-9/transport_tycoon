from data import routes_data


def trains_menu(trains):
    print("trains:")
    print("-"*113)
    print(f"|{"train name":<20} | {"train capacaty":>20}| {"current route id":>20} | {"route percentage":>20}|  {"passenger cars":>20}|")
    print("-"*113)
    for train in trains.values():
        trainCapacityString = str(train["CurrentPeople"]) + "/" + str(train["maxCapacity"])
        print(f"|{train["name"]:<20} | {trainCapacityString:>20}| {routes_data()[train["currentRoutId"]]["name"]:>20} | {str(train["percentageRoute"]) + "%":>20}|  {train["passengerCars"]:>20}|")
    print("-"*113)
    print("Type 'q' to go back| 1 or 'add' add | 2 or 'edit' to edit  | 3 or 'delete' to delete")

    inp = input()

    match inp:
        case "q":
            pass
        case "1" | "add":
            add_train()
        case "2" | "edit":
            edit_train()
        case "3" | "delete":
            delete_train()
        case _:
            trains_menu(trains)


def add_train():
    print("route has been added")


def edit_train():
    print("route has been edited")


def delete_train():
    print("route has been deleted")
