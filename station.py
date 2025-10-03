from data import city_data


def stations_menu(stations, city):
    print("stations")
    print("-"*66)
    print(f"|{"station name":<20} | {"waiting passengers":>20}|{"amount of routs":>20}|")
    print("-"*66)
    for station in stations.values():
        print(f"|{station["name"]:<20} | {station["waitingPassangers"]:>20}|{station["amountOfRoutes"]:>20}|")
    print("-"*66)
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
            delete_station(stations, city)
        case _:
            stations_menu(stations, city)


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


def delete_station(stations, city):
    listOfStations = []
    for station in stations:
        listOfStations.append(station)
        print(
            f"index: {station} \t | station name: {stations[station]["name"]}")
    inp = input("give a station index to delete\n")
    if inp == "q":
        pass
    elif not inp.isdigit():
        print("please give a proper index\n")
        delete_station(stations, city)
    else:
        the_city = str(stations[listOfStations[int(inp)]]["cityId"])
        city.update({
            the_city: {
                "name": city[the_city]["name"],
                "population":  city[the_city]["population"],
                "hasStation": False,
            }})
        stations.pop(inp)
        print("station deleted \n")
        return stations, city
