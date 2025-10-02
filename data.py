def stations_data():
    stations = {
        "0": {
            "name": "test1",
            "waitingPassangers": 50,
            "cityId": "0",
            "amountOfRoutes": 1,
        },
        "1": {
            "name": "test2",
            "waitingPassangers": 50,
            "cityId": "2",
            "amountOfRoutes": 2,
        },
    }
    return stations


def routes_data():
    routes = {
        "0": {
            "name": "test1",
            "expectedPeople": 100,
            "stations": [0, 1],
            "trains": [0],
        },
        "1": {
            "name": "test2",
            "expectedPeople": 50,
            "stations": [1, 0],
            "trains": [1],
        }
    }
    return routes


def trains_data():
    trains = {
        "0": {
            "name": "test1",
            "maxCapacity": 800,
            "CurrentPeople": 400,
            "currentRoutId": "0",
            "percentageRoute": 40,
            "passengerCars": 20,
        },
        "1": {
            "name": "test1",
            "maxCapacity": 1600,
            "CurrentPeople": 800,
            "currentRoutId": "1",
            "percentageRoute": 80,
            "passengerCars": 40,
        }
    }
    return trains


def city_data():
    cities = {
        "0": {
            "name": "test",
            "population": 10000,
            "hasStation": True,
            "station": "0"
        },
        "1": {
            "name": "test1",
            "population": 10000,
            "hasStation": False
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
            "hasStation": False
        },
        "4": {
            "name": "test4",
            "population": 10000,
            "hasStation": False
        }
    }
    return cities
