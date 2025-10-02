def routes_menu(routs, stations):
    print("routes:")
    total = 0
    for route in routs.values():
        print(f"{route['name']:<31} | {route['expectedPeople']:>10} | {len(route['trains']):>5}")
        total += route["expectedPeople"]
    print(f"{total} total passangers")
    print("Type 'q' to go back| 1 or 'add' add | 2 or 'edit' to edit  | 3 or 'delete' to delete")

    inp = input()

    match inp:
        case "q":
            pass
        case "1" | "add":
            add_rout(routs, stations)
        case "2" | "edit":
            edit_route()
        case "3" | "delete":
            delete_route()
        case _:
            routes_menu(routs, stations)


def add_rout(routs, stations):
    complete_station_list = []
    add_station_list = []
    want_to_add_station = True
    for station in stations:
        complete_station_list.append(station)
        print(station, stations[station]["name"])
    while want_to_add_station:
        inp = input("add station by index, press q to stop adding stations")
        if inp == "q" or len(complete_station_list) == len(add_station_list):
            want_to_add_station = False
        elif not inp.isdigit():
            print("please put in a number")
        elif int(inp) > len(add_station_list):
            print("please put in a number thats within the index range")
        elif complete_station_list[int(inp)] in add_station_list:
            print("please dont add a station twice")
        else:
            add_station_list.append(complete_station_list[int(inp)])
            print("station has been added")
    routsAmmount = int(list(routs)[-1]) + 1
    name = "route " + str(routsAmmount)
    routs.update({
        routsAmmount: {
            "name": name,
            "expectedPeople": 100,
            "stations": add_station_list,
            "trains": [],
        }
    })
    print("rout has been added")
    return routs


def edit_route():
    print("route has been edited")


def delete_route():
    print("route has been deleted")
