def trains_menu(trains):
    print("trains:")
    for train in trains.values():
        print(f"""{train["name"]} \t | {train["CurrentPeople"]}/{train["maxCapacity"]} \t | {train["currentRout"]} {train["percentageRoute"]}% \t |  {train["passengerCars"]} """)
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