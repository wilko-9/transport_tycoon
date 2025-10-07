def spawn_passangers(cities, stations):
    for city in cities.values():
        if city["hasStation"]:
            # ToDo: fix random value jump
            currentStation = stations[city["station"]]
            if stations[city["station"]]["amountOfRoutes"] > 0:
                waitingPassangers = currentStation["waitingPassangers"] + (city["population"] / 10) / (1 + currentStation["waitingPassangers"])
                currentStation.update({"waitingPassangers" : int(waitingPassangers)})

    return stations