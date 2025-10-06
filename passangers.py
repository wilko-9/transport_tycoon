def spawn_passangers(cities, stations):
    for city in cities.values():
        print()
        if city["hasStation"]:
            currentStation = stations[city["station"]]
            waitingPassangers = currentStation["waitingPassangers"] + (city["population"] / 100) / (1 + currentStation["waitingPassangers"])
            currentStation.update({"waitingPassangers" : int(waitingPassangers)})

    return stations
