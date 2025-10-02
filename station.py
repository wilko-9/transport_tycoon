from data import city_data


def stations_menu(stations, city):
    print("stations")
    for station in stations.values():
        print(f"""{station["name"]} \t | {station["waitingPassangers"]} \t |  {station["amountOfRoutes"]} """)
    print("Type 'q' to go back| 1 or 'add' add | 2 or 'edit' to edit  | 3 or 'delete' to delete")

    inp = input()

    match inp:
        case "q":
            pass
        case "1" | "add":
            add_station(stations, city)
        case "2" | "edit":
            edit_station()
        case "3" | "delete":
            delete_station(stations)
        case _:
            stations_menu(stations)


def add_station(stations, city):
    cityNoStation = []
    index = 0
    for cityI in city_data():
        if not city_data()[cityI]["hasStation"]:
            cityNoStation.append(cityI)
            print(f"index {index} {str(city_data()[cityI]["name"])}")
            index += 1
    inp = input("please select a index\n")
    if inp == "q":
        pass
    elif not inp.isdigit():
        print("please chose a proper option")
        add_station(stations, city)
    elif int(inp) < len(cityNoStation):
        cityId = cityNoStation[int(inp)]
        StationsAmmount = int(list(stations)[-1]) + 1
        name = 'test' + str(StationsAmmount)
        stations.update({
            StationsAmmount: {
                "name": name,
                "cityId": cityId,
                "expectedPeople": 100,
                "amountOfRoutes": 1,
            }})
        city.update({
            cityId: {
                "name": city[cityNoStation[int(inp)]]["name"],
                "population":  city[cityNoStation[int(inp)]]["population"],
                "hasStation": True,
            }})
        return stations, city
    else:
        print("please chose a proper option")
        add_station(stations, city)


def edit_station():
    print("station has been edited")


def delete_station(stations):
    pass