import settings


def maintenance(stations, trains, routes) -> int:
    """Calculate total maintenance cost based on age of stations, trains, and routes."""
    total_cost = 0

    for station in stations:
        station.age += 1
        if station.age % settings.maintenanceTime == 0:
            total_cost += settings.maintenanceCost

    for train in trains:
        train.age += 1
        if train.age % settings.maintenanceTime == 0:
            total_cost += settings.maintenanceCost

    for route in routes:
        route.age += 1
        if route.age % settings.maintenanceTime == 0:
            total_cost += settings.maintenanceCost

    return total_cost
