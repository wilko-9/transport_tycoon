def stations_menu(stations):
    print("stations")
    for station in stations.values():
        print(f"""{station["name"]} \t | {station["expectedPeople"]} \t |  {station["amountOfRoutes"]} """)
    print("Type 'q' to go back| 1 or \"add\" add | 2 or \"edit\" to edit  | 3 or \"delete\" to delete")
