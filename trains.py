import settings

class Train:
    train_counter = 0  # for auto IDs

    def __init__(self, name, passenger_cars, route=None):
        self.id = Train.train_counter
        Train.train_counter += 1

        self.name = name
        self.passenger_cars = passenger_cars
        self.max_capacity = passenger_cars * 40
        self.current_people = 0
        self.route = route  # Route object or None
        self.percentage_route = 0
        self.previous_station = None
        self.age = 0

        # calculate initial cost for reference (used when selling)
        self.cost = settings.trainPrice + passenger_cars * settings.carPrice

    def edit_train(self, money):
        # Rename train
        new_name = input(f"Current name is '{self.name}'. Enter new name (blank to keep): ").strip()
        if new_name:
            self.name = new_name

        # Edit passenger cars
        add_cars = input(f"Current cars: {self.passenger_cars}. Add/remove cars? Enter number or 0: ").strip()
        if add_cars.isdigit():
            add_cars = int(add_cars)
            if add_cars != 0:
                self.passenger_cars += add_cars
                money -= add_cars * settings.carPrice
                self.max_capacity = self.passenger_cars * 40
                self.cost += add_cars * settings.carPrice
                print(f"Passenger cars updated to {self.passenger_cars}. Money left: {money}")
        return money

    def assign_route(self, route):
        self.route = route
        print(f"Train '{self.name}' assigned to route '{route.name}'.")

    def move_train(self, money):
        if not self.route or not self.route.stations:
            return money  # nothing to do

        self.percentage_route += 5  # percentage of route completed
        if self.percentage_route >= 100:
            # Determine next station
            route_stations = self.route.stations
            if self.previous_station is None:
                self.previous_station = route_stations[-1]

            index = route_stations.index(self.previous_station) + 1
            if index >= len(route_stations):
                index = 0  # loop back to start
            station = route_stations[index]

            self.previous_station = station
            self.percentage_route = 0

            # Unload passengers and earn money
            money += self.current_people * 5  # Example revenue
            self.current_people = 0

            # Load passengers
            if self.max_capacity >= station.waiting_passengers:
                self.current_people = station.waiting_passengers
                station.waiting_passengers = 0
            else:
                self.current_people = self.max_capacity
                station.waiting_passengers -= self.max_capacity
        return money

    def sell_train(self, money):
        refund = int(self.cost * 0.8)
        money += refund
        print(f"Train '{self.name}' sold for ${refund}")
        return money

    def __str__(self):
        route_name = self.route.name if self.route else "No route"
        return (f"{self.name} | Cars: {self.passenger_cars} | Capacity: {self.current_people}/{self.max_capacity} | "
                f"Route: {route_name} | {self.percentage_route}% completed")

# -----------------------------
# Example menu functions
# -----------------------------

def trains_menu(trains, routes, money):
    while True:
        print("\nTrains:")
        print("-" * 120)
        print(f"| {'ID':<5} | {'Name':<20} | {'Cars':>5} | {'Capacity':>10} | {'Route':<20} | {'Progress':>10} |")
        print("-" * 120)
        for train in trains:
            route_name = train.route.name if train.route else "None"
            cap_str = f"{train.current_people}/{train.max_capacity}"
            print(f"| {train.id:<5} | {train.name:<20} | {train.passenger_cars:>5} | {cap_str:>10} | {route_name:<20} | {train.percentage_route:>10}% |")
        print("-" * 120)
        print(f"Money: ${money}")
        print("Type 'q' to go back | 1 add | 2 edit | 3 delete")

        inp = input("> ").strip().lower()
        match inp:
            case "q":
                break
            case "1" | "add":
                money = add_train(trains, money, routes)
            case "2" | "edit":
                money = edit_train(trains, money, routes)
            case "3" | "delete":
                money = delete_train(trains, money, routes)
        return money

def add_train(trains, money, routes):
    name = input("Enter train name: ").strip()
    passenger_cars = int(input("Enter number of passenger cars: ").strip())

    total_cost = settings.trainPrice + passenger_cars * settings.carPrice
    if money < total_cost:
        print(f"Not enough money! Train costs ${total_cost}, you have ${money}.")
        return money

    train = Train(name, passenger_cars)
    money -= total_cost

    assign_route = input("Assign to a route? (yes/no): ").strip().lower()
    if assign_route == "yes":
        if len(routes) > 0:
            for idx, route in enumerate(routes):
                print(f"{idx}: {route.name}")
            choice = int(input("Select route index: "))
            if choice in routes:  # TODO: add better validation
                train.assign_route(routes[choice])
        else:  # TODO: send to route creation
            print("There are no routes. Please add one in the route menu")

    trains.append(train)
    print(f"Train '{train.name}' added. Money left: ${money}")
    return money

def edit_train(trains, money, routes):
    for train in trains:
        print(f"{train.id}: {train.name}")
    choice = int(input("Select train ID to edit: "))
    train = next((t for t in trains if t.id == choice), None)
    if train:
        money = train.edit_train(money)
    return money

def delete_train(trains, money, routes):
    for train in trains:
        print(f"{train.id}: {train.name}")
    choice = int(input("Select train ID to delete: "))
    train = next((t for t in trains if t.id == choice), None)
    if train:
        money = train.sell_train(money)
        trains.remove(train)
    return money

def move_trains(trains, money):
    for train in trains:
        money = train.move_train(money)
    return money
