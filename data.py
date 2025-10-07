def stations_data():
    stations = {
        "0": {
            "name": "test1",
            "waitingPassangers": 50,
            "cityId": "0",
            "amountOfRoutes": 1,
            "age" : 0
        },
        "1": {
            "name": "test2",
            "waitingPassangers": 50,
            "cityId": "2",
            "amountOfRoutes": 2,
            "age" : 0
        }
    }
    return stations


def routes_data():
    routes = {
        "0": {
            "name": "test1",
            "expectedPeople": 100,
            "stations": [0, 1],
            "trains": [0],
            "age" : 0
        },
        "1": {
            "name": "test2",
            "expectedPeople": 50,
            "stations": [1, 0],
            "trains": [1],
            "age" : 0
        }
    }
    return routes


def trains_data():
    # ToDo: percantageRoute should be metersOnRoute for actual distance calculations
    trains = {
        "0": {
            "name": "test1",
            "maxCapacity": 800,
            "CurrentPeople": 400,
            "currentRouteId": 0,
            "percentageRoute": 40,
            "passengerCars": 20,
            "age" : 0,
            "previousStation" : 0
        },
        "1": {
            "name": "test2",
            "maxCapacity": 1600,
            "CurrentPeople": 800,
            "currentRouteId": 1,
            "percentageRoute": 80,
            "passengerCars": 40,
            "age" : 0,
            "previousStation" : 1
        }
    }
    return trains


def city_data():
    cities = {
        "0": {
            "name": "test",
            "population": 10000,
            "hasStation": True,
            "station": "0"# ToDo: just make this station : NULL if it doesnt have a station. removes the need for hasStation
        },
        "1": {
            "name": "test1",
            "population": 10000,
            "hasStation": False,
            "station": None
        },
        "2": {
            "name": "test2",
            "population": 10000,
            "hasStation": True,
            "station": "1"
        },
        "3": {
            "name": "test3",
            "population": 10000,
            "hasStation": False,
            "station": None
        },
        "4": {
            "name": "test4",
            "population": 10000,
            "hasStation": False,
            "station": None
        }
    }
    return cities
