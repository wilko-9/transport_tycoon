def StationsData():
    stations = {
        "0": {
            "name": "test1",
            "expectedPeople": 100,
            "amountOfRoutes": 1,
        },
        "1": {
            "name": "test2",
            "expectedPeople": 50,
            "amountOfRoutes": 2,
        }
    }
    return stations


def routesData():
    routes = {
        "0": {
            "name": "test1",
            "expectedPeople": 100,
            "trains": [0],
        },
        "1": {
            "name": "test2",
            "expectedPeople": 50,
            "trains": [1],
        }
    }
    return routes


def trainsData():
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
