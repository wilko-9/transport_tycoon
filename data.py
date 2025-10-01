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
            "amountOfTrains": 1,
        },
        "1": {
            "name": "test2",
            "expectedPeople": 50,
            "amountOfTrains": 2,
        }
    }
    return routes


def trainsData():
    trains = {
        "0": {
            "name": "test1",
            "maxCapacity": 800,
            "CurrentPeople": 400,
            "percentageRoute": 40,
            "passengerCars": 20,
        },
        "1": {
            "name": "test1",
            "maxCapacity": 1600,
            "CurrentPeople": 800,
            "percentageRoute": 80,
            "passengerCars": 40,
        }
    }
    return trains
