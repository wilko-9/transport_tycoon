def cities_menu(cities):
    for city in cities:
        if city["hasStation"]:
            hasStation = "This city has a station"
        else:
            hasStation = "This city does not have a station"

        print(f"{city["name"]} | population: {city["population"]} | {hasStation}")
        print("Type 'quit' to go back")
    
    match input(""):
        case "q":
            pass
        case _:
            cities_menu(cities)

def new_city(cities):
    cityAmmount = len(cities)
    name = 'test' + str(cityAmmount)
    population = range(5000, 50000)
    cities.add({
        cityAmmount: {
            "name": name,
            "population": population,
            "hasStation": False
        }
    })
    
    return cities