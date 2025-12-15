class Route:
    route_counter = 0  # class variable to auto-assign route IDs

    def __init__(self, name=None, stations=None):
        if stations is None:
            stations = []
        self.id = Route.route_counter
        Route.route_counter += 1

        self.name = name if name else f"Route {self.id}"
        self.stations = stations  # list of Station objects or None
        self.trains = []          # list of train objects
        self.expected_people = 0
        self.age = 0

    def add_station(self, station):
        """Add a station to the route if not already included."""
        if station not in self.stations:
            self.stations.append(station)
            print(f"Station '{station.name}' added to route '{self.name}'.")
        else:
            print(f"Station '{station.name}' is already on the route.")

    def remove_station(self, station):
        """Remove a station from the route."""
        if station in self.stations:
            self.stations.remove(station)
            print(f"Station '{station.name}' removed from route '{self.name}'.")
        else:
            print(f"Station '{station.name}' is not on the route.")

    def calculate_passengers(self, trains):
        """Calculate total passengers on the route based on assigned trains."""
        total = 0
        for train in self.trains:
            # train can be a Train object or an ID mapping to the trains dictionary
            if isinstance(train, int) and str(train) in trains:
                total += trains[str(train)]["CurrentPeople"]
            elif hasattr(train, "current_people"):
                total += train.current_people
        return total

    def __str__(self):
        return f"{self.name} | Stations: {len(self.stations)} | Trains: {len(self.trains)}"


# -----------------------------
# Updated menu functions
# -----------------------------

def routes_menu(routes, stations, trains):
    print("Routes:")
    print("-" * 63)
    print(f"|{'Name':<20} | {'People Traveling':>20} | {'Trains on Route':>15}|")
    print("-" * 63)

    total_passengers = 0
    for route in routes:
        passengers = route.calculate_passengers(trains)
        print(f"|{route.name:<20} | {passengers:>20} | {len(route.trains):>15}|")
        total_passengers += passengers

    print("-" * 63)
    print(f"{total_passengers} total passengers")
    print("Type 'q' to go back | 1 or 'add' add | 2 or 'edit' to edit | 3 or 'delete' to delete")

    choice = input("> ").strip().lower()
    match choice:
        case "q":
            return
        case "1" | "add":
            add_route(routes, stations)
        case "2" | "edit":
            edit_route(routes)
        case "3" | "delete":
            delete_route(routes)
        case _:
            routes_menu(routes, stations, trains)


def add_route(routes, stations):
    """Create a new route by selecting stations."""
    route_stations = []
    route_name = input("give your route a name.")
    while True:
        if len(stations) > 0:
            print("Available stations:")
            for idx, station in enumerate(stations):
                print(f"{idx}: {station.name}")

            inp = input("Add station by index (q to finish): ").strip()
            if inp.lower() == "q":
                break
            if not inp.isdigit() or int(inp) >= len(stations):
                print("Invalid input.")
                continue
            station = stations[int(inp)]
            if station in route_stations:
                print("Station already added to route.")
                continue
            route_stations.append(station)
            print(f"Station '{station.name}' added to route.")
        else:
            break

    new_route = Route(name=route_name, stations=route_stations)
    routes.append(new_route)
    print(f"Route '{new_route.name}' has been created.")
    print("returning to menu")
    return new_route


def edit_route(routes):
    if not routes:
        print("No routes to edit.")
        return
    print("Select a route to edit:")
    for idx, route in enumerate(routes):
        print(f"{idx}: {route}")

    inp = input("> ").strip()
    if not inp.isdigit() or int(inp) >= len(routes):
        print("Invalid input.")
        return

    selected_route = routes[int(inp)]
    print(f"Editing route '{selected_route.name}'")
    # Example: rename route
    new_name = input("Enter new name (leave blank to keep current): ").strip()
    if new_name:
        selected_route.name = new_name
        print(f"Route renamed to '{selected_route.name}'.")


def delete_route(routes):
    if not routes:
        print("No routes to delete.")
        return
    print("Select a route to delete:")
    for idx, route in enumerate(routes):
        print(f"{idx}: {route}")

    inp = input("> ").strip()
    if not inp.isdigit() or int(inp) >= len(routes):
        print("Invalid input.")
        return

    removed_route = routes.pop(int(inp))
    print(f"Route '{removed_route.name}' has been deleted.")
