from data import city_data


def stations_menu(stations):
    print("stations")
    for station in stations.values():
        print(f"""{station["name"]} \t | {station["expectedPeople"]} \t |  {station["amountOfRoutes"]} """)
    print("Type 'q' to go back| 1 or 'add' add | 2 or 'edit' to edit  | 3 or 'delete' to delete")

    inp = input()

    match inp:
        case "q":
            pass
        case "1" | "add":
            add_station(stations)
        case "2" | "edit":
            edit_station()
        case "3" | "delete":
            delete_station(stations)
        case _:
            stations_menu(stations)


def add_station(stations):
    cityNoStation = []
    index = 0
    for city in city_data():
        if not city_data()[city]["hasStation"]:
            cityNoStation.append(city)
            print(f"index {index} {str(city_data()[city]["name"])}")
            index += 1
    inp = input("please select a index\n")
    if inp == "q":
        pass
    elif not inp.isdigit():
        print("please chose a proper option")
        add_station()
    elif int(inp) < len(cityNoStation):
        cityId = 0
        StationsAmmount = int(list(stations)[-1]) + 1
        print(cityNoStation[int(inp)])
        name = 'test' + str(StationsAmmount)
        stations.update({
            StationsAmmount: {
                "name": name,
                "cityId": cityId,
                "expectedPeople": 100,
                "amountOfRoutes": 1,
            }})
        return stations
    else:
        print("please chose a proper option")
        add_station()


def edit_station():
    print("station has been edited")


def delete_station(stations):
    pass