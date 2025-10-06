from data import routes_data

def trains_menu(trains, money):
    print("trains:")
    for train_id, train in trains.items():
        if train["currentRouteId"] == None:
            route = "This train is not assigned to a route"
        else:
            route = routes_data()[str(train["currentRouteId"])]["name"]
        print(f"""ID: {train_id} | name: {train["name"]} \t | passangers: {train["CurrentPeople"]}/{train["maxCapacity"]} \t | route: {route} {train["percentageRoute"]}% \t |  cars: {train["passengerCars"]} | age: {train["age"]}""")
    print("Type 'q' to go back| 1 or 'add' add | 2 or 'edit' to edit  | 3 or 'delete' to delete")

    inp = input()

    match inp:
        case "q":
            return trains
        case "1" | "add":
            return add_train(trains, money)
        case "2" | "edit":
            return edit_train(trains, money)
        case "3" | "delete":
            return delete_train(trains, money)
        case _:
            return trains_menu(trains, money)


def add_train(trains, money):
    trainIndex = int(list(trains)[-1]) + 1
    carPrice = 100
    trainPrice = 500
    name = input("what should the name of your train be?")
    try:
        passengerCars = int(input("How many cars should your train have?"))
    except ValueError:
        print("Invalid number. Please try again.")
        return add_train(trains, money)
    routeId = None

    if input("Would you like to add this train to a route? (yes/no): ").lower() == "yes":
        routeId = input("What route shall this train follow? Please enter its route ID")
        if routeId in routes_data():
            routeId = int(routeId)
            print(f"Route set to {routeId}.")
        else:
            print("Route not found. Please edit the train to add the route.")

    price = trainPrice + passengerCars * carPrice
    if price <= money:
        trains.update({
            
            trainIndex : {
                "name": name,
                "maxCapacity": int(passengerCars)*40,
                "CurrentPeople": 0,
                "currentRouteId": routeId,
                "percentageRoute": 0,
                "passengerCars": passengerCars,
                "age" : 0
            }
        })
        money -= price

        print(f"Train has been created with {passengerCars} cars at the cost of {price}")
    else:
        print("You don't have enough money to buy this train")
    return trains


def edit_train(trains, money):
    trainId = input("Please enter the ID of the train that you would like to edit: ")
    
    if trainId in trains:
        train = trains[trainId]
        
        if input("Would you like to edit the amount of cars? (yes/no): ").lower() == "yes":
            try:
                new_cars = int(input("Enter the new number of passenger cars: "))
                difference = new_cars - train["passangerCars"]

                train["passengerCars"] = new_cars
                print(f"Updated passenger cars to {new_cars}.")
            except ValueError:
                print("Invalid number. Please try again.")
                return edit_train(trains, money)

        elif input("Would you like to edit the name? (yes/no): ").lower() == "yes":
            new_name = input("What would you like to call your train? ")
            train["name"] = new_name
            print(f"Train name updated to {new_name}.")

        elif input("Would you like to edit this train's route? (yes/no): ").lower() == "yes":
            try:
                routeId = input("What route shall this train follow? Please enter its route ID")
                if routeId in routes_data():
                    routeId = int(routeId)
                    train["currentRouteId"] = routeId
                    print(f"Route updated to {routeId}.")
                elif routeId == "none":
                        train["currentRouteId"] = None
                        print(f"Route updated to None.")  
                else:
                    print("No route with found with given ID. Please try again.")
                    edit_train(trains, money)
            except ValueError:
                print("Invalid number. Please try again.")
                edit_train(trains, money)
        
        else:
            print("There are no other options. You will now return to the main menu.")
    else:
        print("The given ID was not found. Please try again.")
        edit_train(trains, money)

    return trains


def delete_train(trains, money):
    trainID = input("what train would you like to delete?")
    if trainID in trains:
        train = trains[trainID]
        if input(f"are you sure that you want to delete train {trainID}? and all {train["passengerCars"]} of its cars? (yes/no): ").lower() == "yes":
            del train
            print("Train deleted succesfully")
            return trains
    else:
        print("Train not found. Returning you to the main menu.")
        return trains