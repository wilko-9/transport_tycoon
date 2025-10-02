def spawn_passangers(cities, stations):
    print("Hallo")
    for city in cities.values():
        if city["hasStation"]:
            currentStation = stations[city["station"]]
            waitingPassangers = currentStation["waitingPassangers"] + (city["population"] / 100) / (1 + currentStation["waitingPassangers"])
            print(waitingPassangers)
            currentStation.update({"waitingPassangers" : int(waitingPassangers)})
            print(currentStation)
    return stations