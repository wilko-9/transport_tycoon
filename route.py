def routes_menu(routes, stations, trains):
    print("routes:")
    print("-" * 74)
    print(f"|{"id":<10}|{"name":<20} | {"people traveling":>20} | {"trains on route":>15}|")
    print("-" * 74)
    total = 0
    for route in routes:
        passengersOnRoute = 0
        for train in routes[route]['trains']:
            passengersOnRoute += trains[str(train)]["CurrentPeople"]
        print(
            f"|{route:<10}|{routes[route]['name']:<20} | {passengersOnRoute:>20} | {len(routes[route]['trains']):>15}|")
        total += passengersOnRoute
    print("-" * 74)
    print(f"{total} total passangers")
    print("Type 'q' to go back| 1 or 'add' add | 2 or 'edit' to edit  | 3 or 'delete' to delete")

    inp = input()

    match inp:
        case "q":
            pass
        case "1" | "add":
            add_rout(routes, stations)
        case "2" | "edit":
            edit_route(routes)
        case "3" | "delete":
            delete_route()
        case _:
            routes_menu(routes, stations, trains)


def add_rout(routes, stations):
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
    routesAmmount = int(list(routes)[-1]) + 1
    name = "route " + str(routesAmmount)
    routes.update({
        routesAmmount: {
            "name": name,
            "expectedPeople": 100,
            "stations": add_station_list,
            "trains": [],
        }
    })
    print("rout has been added")
    return routes


def edit_route(routes):
    routeId = input(
        "Please enter the ID of the route that you would like to edit: ")
    
    if routeId in routes:
        print(routeId)
        if input("would you like to give the the route a new name? (yes/no): ").lower() == "yes":
            newName = input("give the route a new name")
            routes[routeId]["name"] = newName
    else:
        print("The given ID was not found. Please try again.")
        edit_route(routes)

def delete_route():
    print("route has been deleted")
