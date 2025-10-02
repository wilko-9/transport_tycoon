# loop trough all owned buildings, routes and veichles. 
# Add one day to their age and check if its devisible by 20. 
# If it is, charge maintenance.
def maintenance(stations, trains, routes) -> int:
    stationCost = 0
    trainCost = 0 
    routeCost = 0
    # how many days must have passed untill the services need 
    # to be maintained
    maintenanceTime = 20
    # How much it costs to maintain the services
    maintenanceCost = 50
    for station in stations.values():
        station["age"] += 1
        if station["age"] % maintenanceTime == 0:
            stationCost += maintenanceCost

    for train in trains.values():
        train["age"] += 1
        if train["age"] % maintenanceTime == 0:
            trainCost += maintenanceCost

    for route in routes.values():
        print(route["age"])
        route["age"] += 1
        if route["age"] % maintenanceTime == 0:
            routeCost += maintenanceCost

    totalCost = stationCost + trainCost + routeCost
    return totalCost