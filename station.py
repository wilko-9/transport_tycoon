import settings

class Station:
    def __init__(self, city, name, platforms):
        self.city = city
        self.name = name
        self.platforms = platforms
        self.tier = 0
        self.waiting_passengers = 0
        self.amount_of_routes = 0
        self.age = 0
        # calculate initial cost for reference (used when selling)
        self.cost = settings.stationPrice + (platforms -1) * settings.platformPrice

    def edit_station(self):
        print(f"Editing station '{self.name}' in city '{self.city.name}'")
        new_name = input("Enter new name (or leave blank to keep current): ").strip()
        if new_name:
            self.name = new_name

        add_platforms = input("Enter number of extra platforms to add (or 0 to skip): ").strip()
        if add_platforms.isdigit() and int(add_platforms) > 0:
            num_platforms = int(add_platforms)
            self.platforms += num_platforms
            self.cost += num_platforms * settings.platformPrice
            print(f"{num_platforms} platforms added. Total platforms: {self.platforms}")
        else:
            print("No platforms added.")

    def delete_station(self, stations, money):
        """Delete this station and refund the user based on saleValue."""
        refund = int(self.cost * settings.saleValue / 100)
        money += refund
        print(f"Station '{self.name}' deleted. You got ${refund} back.")
        self.city.station = None
        if self in stations:
            stations.remove(self)
        return money

    def spawn_passengers(self):
        if self.amount_of_routes > 0:
            waiting = self.waiting_passengers + (self.city.population / 10) / (1 + self.waiting_passengers)
            self.waiting_passengers = int(waiting)


def stations_menu(stations, cities, money):
    while True:
        print("\nStations Menu")
        print("-" * 66)
        print(f"|{'Station Name':<20} | {'City':<20} | {'Platforms':>10} |")
        print("-" * 66)
        for station in stations:
            print(f"|{station.name:<20} | {station.city.name:<20} | {station.platforms:>10} |")
        print("-" * 66)
        print("Type 'q' to go back | 1 to add | 2 to edit | 3 to delete")
        choice = input("> ").strip().lower()

        match choice:
            case "1" | "add":
                # Add new station
                cities_no_station = [city for city in cities if city.station is None]

                if not cities_no_station:
                    print("All cities already have stations. Cannot add a new station.")
                    continue

                print("Select a city to add a station (q to cancel):")
                for idx, city in enumerate(cities_no_station):
                    print(f"{idx}: {city.name} (Population: {city.population})")

                city_choice = input("> ").strip()
                if city_choice.lower() == "q":
                    continue
                if not city_choice.isdigit() or int(city_choice) >= len(cities_no_station):
                    print("Invalid selection.")
                    continue

                selected_city = cities_no_station[int(city_choice)]
                station_name = input("Enter station name: ").strip()
                platforms = int(input("Enter number of platforms: ").strip())

                total_cost = settings.stationPrice + (platforms -1) * settings.platformPrice
                if money < total_cost:
                    print(f"Not enough money. This station costs ${total_cost}, you have ${money}.")
                    continue

                money -= total_cost
                new_station = Station(selected_city, station_name, platforms)
                selected_city.station = new_station
                stations.append(new_station)
                print(f"Station '{station_name}' added to city '{selected_city.name}'. Remaining money: ${money}")

            case "2" | "edit":
                # Edit an existing station
                if not stations:
                    print("No stations to edit.")
                    continue
                print("Select a station to edit (q to cancel):")
                for idx, station in enumerate(stations):
                    print(f"{idx}: {station.name} (City: {station.city.name}, Platforms: {station.platforms})")

                station_choice = input("> ").strip()
                if station_choice.lower() == "q":
                    continue
                if not station_choice.isdigit() or int(station_choice) >= len(stations):
                    print("Invalid selection.")
                    continue

                selected_station = stations[int(station_choice)]
                # Editing may cost extra for new platforms
                old_money = money
                selected_station.edit_station()
                money_spent = selected_station.cost - (settings.stationPrice + selected_station.platforms * settings.platformPrice)
                if money_spent > money:
                    print("Not enough money to add platforms. Reverting changes.")
                    # Revert platform changes
                    selected_station.platforms -= money_spent // settings.platformPrice
                    selected_station.cost -= money_spent
                else:
                    money -= money_spent
                    print(f"Station edited. Remaining money: ${money}")

            case "3" | "delete":
                # Delete a station
                if not stations:
                    print("No stations to delete.")
                    continue
                print("Select a station to delete (q to cancel):")
                for idx, station in enumerate(stations):
                    print(f"{idx}: {station.name} (City: {station.city.name})")
                station_choice = input("> ").strip()
                if station_choice.lower() == "q":
                    continue
                if not station_choice.isdigit() or int(station_choice) >= len(stations):
                    print("Invalid selection.")
                    continue

                selected_station = stations[int(station_choice)]
                money = selected_station.delete_station(stations, money)
                print(f"Remaining money: ${money}")

            case "q":
                break

    return money
