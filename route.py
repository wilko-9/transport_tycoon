def routes_menu(routs):
    print("routes:")
    total = 0
    for rout in routs.values():
        print(f"""{rout["name"]} \t | {rout["expectedPeople"]} \t |  {rout["amountOfTrains"]} """)
        total += rout["expectedPeople"]
    print(f"{total} total passangers")
    print("Type 'q' to go back| 1 or 'add' add | 2 or 'edit' to edit  | 3 or 'delete' to delete")

    inp = input()

    match inp:
        case "q":
            pass
        case "1" | "add":
            add_rout()
        case "2" | "edit":
            edit_route()
        case "3" | "delete":
            delete_route()
        case _:
            routes_menu(routs)


def add_rout():
    print("route has been added")


def edit_route():
    print("route has been edited")


def delete_route():
    print("route has been deleted")
