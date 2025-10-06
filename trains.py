import settings

def trains_menu(trains, routes, money):
    print("trains:")
    print("-"*135)
    print(f"|{"train ID":<20} |{"train name":<20} | {"train capacaty":>20}| {"current route id":>20} | {"route percentage":>20}|  {"passenger cars":>20}|")
    print("-"*135)
    for train_id, train in trains.items():
        if train["currentRouteId"] == None:
            route = "This train is not assigned to a route"
        else:
            route = routes[str(train["currentRouteId"])]["name"]
        trainCapacityString = str(train["CurrentPeople"]) + "/" + str(train["maxCapacity"])
        print(f"|{train_id:<20} |{train["name"]:<20} | {trainCapacityString:>20}| {route:>20} | {str(train["percentageRoute"]) + "%":>20}|  {train["passengerCars"]:>20}|")
    print("-"*135)
    print("Type 'q' to go back| 1 or 'add' add | 2 or 'edit' to edit  | 3 or 'delete' to delete")

    inp = input()
    

    match inp:
        case "q":
            return trains
        case "1" | "add":
            return add_train(trains, money, routes)
        case "2" | "edit":
            return edit_train(trains, money, routes)
        case "3" | "delete":
            return delete_train(trains, money)
        case _:
            return trains_menu(trains, routes, money)


def add_train(trains, money, routes):
    trainIndex = int(list(trains)[-1]) + 1
    carPrice = settings.carPrice
    trainPrice = settings.trainPrice
    name = input("what should the name of your train be?")
    try:
        passengerCars = int(input("How many cars should your train have?"))
    except ValueError:
        print("Invalid number. Please try again.")
        return add_train(trains, money, routes)
    routeId = None

    if input("Would you like to add this train to a route? (yes/no): ").lower() == "yes":
        routeId = input("What route shall this train follow? Please enter its route ID")
        if routeId in routes:
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
                "age" : 0,
                "previousStation" : None
            }
        })
        money -= price

        print(f"Train has been created with {passengerCars} cars at the cost of {price}")
    else:
        print("You don't have enough money to buy this train")
    return trains


def edit_train(trains, money, routes):
    trainId = input("Please enter the ID of the train that you would like to edit: ")
    
    if trainId in trains:
        train = trains[trainId]
        
        if input("Would you like to edit the amount of cars? (yes/no): ").lower() == "yes":
            try:
                new_cars = int(input("Enter the new number of passenger cars: "))
                difference = new_cars - train["passangerCars"]
                if difference < 0:
                    money = money + difference * int(settings.carPrice * 0.8)
                elif difference > 0:
                    money = money - difference * int(settings.carPrice * 0.8)

                train["passengerCars"] = new_cars
                print(f"Updated passenger cars to {new_cars}.")
            except ValueError:
                print("Invalid number. Please try again.")
                return edit_train(trains, money, routes)

        elif input("Would you like to edit the name? (yes/no): ").lower() == "yes":
            new_name = input("What would you like to call your train? ")
            train["name"] = new_name
            print(f"Train name updated to {new_name}.")

        elif input("Would you like to edit this train's route? (yes/no): ").lower() == "yes":
            try:
                routeId = input("What route shall this train follow? Please enter its route ID")
                if routeId in routes:
                    routeId = int(routeId)
                    train["currentRouteId"] = routeId
                    print(f"Route updated to {routeId}.")
                elif routeId == "none":
                        train["currentRouteId"] = None
                        print(f"Route updated to None.")  
                else:
                    print("No route with found with given ID. Please try again.")
                    edit_train(trains, money, routes)
            except ValueError:
                print("Invalid number. Please try again.")
                edit_train(trains, money, routes)
        
        else:
            print("There are no other options. You will now return to the main menu.")
    else:
        print("The given ID was not found. Please try again.")
        edit_train(trains, money, routes)

    return trains


def delete_train(trains, money):
    trainID = input("what train would you like to delete?")
    if trainID in trains:
        train = trains[trainID]
        if input(f"are you sure that you want to delete train {trainID}? and all {train["passengerCars"]} of its cars? (yes/no): ").lower() == "yes":
            money = money + int(settings.carPrice * 0.8) * int(train["passengerCars"]) + int(settings.trainPrice * 0.8)
            del train
            print("Train deleted succesfully")
            return trains
    else:
        print("Train not found. Returning you to the main menu.")
        return trains

def move_train(trains, money, stations, routes):
    for train in trains.values():
        train["percentageRoute"] += 5
        # if train is at its destination
        if train["percentageRoute"] == 100:
            route = routes[str(train["currentRouteId"])]
            if train["previousStation"] == None:
                train["previousStation"] = route["stations"][-1]# set the previous station to the last station of the route.
            index = route["stations"].index(train["previousStation"]) + 1
            # if previous station was the final station of the route
            if index == len(route["stations"]):
                index = 0
            station = stations[str(index)]
            train["previousStation"] = index
            #unload passangers and add money for delivered passangers
            train["percentageRoute"] = 0
            money += train["CurrentPeople"] * 5 # ToDo: replace 5 with value of the route.
            train["CurrentPeople"] = 0
            #load passangers
            if train["maxCapacity"] >= station["waitingPassangers"]:
                train["CurrentPeople"] = station["waitingPassangers"]
                station["waitingPassangers"] = 0
            else:
                train["CurrentPeople"] = train["maxCapacity"]
                station["waitingPassangers"] -= train["maxCapacity"]
    
    return trains, money