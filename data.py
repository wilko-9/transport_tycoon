import json
import os
from sys import platform


def stations_data():
    stations = {
        "0": {
            "name": "test1",
            "waitingPassangers": 50,
            "cityId": "0",
            "amountOfRoutes": 1,
            "age": 0,
        },
        "1": {
            "name": "test2",
            "waitingPassangers": 50,
            "cityId": "2",
            "amountOfRoutes": 2,
            "age": 0,
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
            "age": 0,
        },
        "1": {
            "name": "test2",
            "expectedPeople": 50,
            "stations": [1, 0],
            "trains": [1],
            "age": 0,
        },
    }
    return routes


def trains_data():
    trains = {
        "0": {
            "name": "test1",
            "maxCapacity": 800,
            "CurrentPeople": 400,
            "currentRouteId": 0,
            "metersOnRoute": 40,
            "passengerCars": 20,
            "age": 0,
            "previousStation": 0,
        },
        "1": {
            "name": "test2",
            "maxCapacity": 1600,
            "CurrentPeople": 800,
            "currentRouteId": 1,
            "metersOnRoute": 80,
            "passengerCars": 40,
            "age": 0,
            "previousStation": 1,
        },
    }
    return trains


def city_data():
    cities = {
        "0": {
            "name": "test",
            "population": 10000,
            "hasStation": True,
            "station": "0",  # ToDo: just make this station : NULL if it doesnt have a station. removes the need for hasStation
        },
        "1": {
            "name": "test1",
            "population": 10000,
            "hasStation": False,
            "station": None,
        },
        "2": {"name": "test2", "population": 10000, "hasStation": True, "station": "1"},
        "3": {
            "name": "test3",
            "population": 10000,
            "hasStation": False,
            "station": None,
        },
        "4": {
            "name": "test4",
            "population": 10000,
            "hasStation": False,
            "station": None,
        },
    }
    return cities


"""
loads in the current game save data
TODO:
    - check for if there is no file
    - check for in correct data
"""


def load_game_data():
    file_directory = os.path.dirname(os.path.realpath(__file__))
    if platform == "win32" or platform == "cygwin":
        save = file_directory + "\\saves.json"
    else:
        save = file_directory + "/saves.json"
    with open(save) as f:
        theData = json.load(f)
    current_save = theData
    return current_save


"""
condenses all data to be send to the save file
TODO:
    - still needs validation of data
"""


def save_parser(cities, stations, routes, trains, days, money, gameSettings, saveName):
    save_index = "0"
    save = {
        save_index: {
            "name": saveName,
            "days": days,
            "money": money,
            "gameSettings": gameSettings,
            "cities": cities,
            "stations": stations,
            "routes": routes,
            "trains": trains,
        }
    }
    return json.dumps(save, indent=4)


def write_save_data(
    cities, stations, routes, trains, days, money, gameSettings, saveName
):
    saveWrite = save_parser(
        cities, stations, routes, trains, days, money, gameSettings, saveName
    )
    file_directory = os.path.dirname(os.path.realpath(__file__))
    if platform == "win32" or platform == "cygwin":
        save = file_directory + "\\saves.json"
    else:
        save = file_directory + "/saves.json"
    with open(save, "w") as f:
        f.write(saveWrite)


def in_memory_save(name, setting, cities):
    return {
        "name": name,
        "days": 0,
        "money": setting["startingMoney"],
        "gameSettings": setting,
        "cities": cities,
        "stations": {},
        "routes": {},
        "trains": {},
    }
