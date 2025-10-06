import random

def cities_menu(cities):
    print("-"*83)
    print(f"|{"city name":<20} | {"population":>20} | {"does the city has a station?":>35}|")
    print("-"*83)
    for city in cities.values():
        if city["hasStation"]:
            hasStation = "This city has a station"
        else:
            hasStation = "This city does not have a station"
        print(f"|{city["name"]:<20} | {str(city["population"]):>20} | {hasStation:<35}|")
    print("-"*83)
    print("Type 'quit' to go back")
    
    match input(""):
        case "q":
            pass
        case _:
            cities_menu(cities)

# create a new city with a random name and a random population ranging from 5000 to 50000
def new_city(cities):
    cityAmmount = len(cities)
    name = 'test' + str(cityAmmount)
    population = random.randint(5000, 50000)
    cities.update({
        cityAmmount: {
            "name": name,
            "population": population,
            "hasStation": False
        }
    })
    print(f"A new city with the name {name} has been founded! It has a population of {population} people")
    return cities

#grow a random city by a random number, ranging from 1000 to 10000
def grow_city(cities):
    city = cities[str(random.randint(0,len(cities)-1))] # Decide what city should grow
    city["population"] += random.randint(1000, 10000)
    print(f"The city {city["name"]} has grown! It now has a population of {city["population"]} people")
    return cities
