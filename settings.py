# how many days must have passed untill the services need to be maintained
maintenanceTime = 20
# How much it costs to maintain the services
maintenanceCost = 50
# How much it costs to buy a train
trainPrice = 500
# How much it costs to buy a train car
carPrice = 100
# Ammount of cash the player starts with
startingMoney = 50000

# ToDo: add all const variables in this file for easy game balance changes


# combines the original settingds:
def default_setting():
    return {
        "maintenanceTime": maintenanceTime,
        "maintenanceCost": maintenanceCost,
        "trainPrice": trainPrice,
        "carPrice": carPrice,
        "startingMoney": startingMoney,
    }


def settings_menu():
    settings = default_setting()
    while True:
        maintenanceTimeInput = input(
            f"""maintenance time in days 
default: {settings["maintenanceTime"]} days
leave empty for default
"""
        )
        if not maintenanceTimeInput:
            print("using default")
            break
        if not str(maintenanceTimeInput).isdigit():
            print("please put a numeric value")
        else:
            settings["maintenanceTime"] = int(maintenanceTimeInput)
            break
    while True:
        maintenanceCostInput = input(
            f"""maintenance cost 
default: {settings["maintenanceCost"]} money
leave empty for default
"""
        )
        if not maintenanceCostInput:
            print("using default")
            break
        if not str(maintenanceCostInput).isdigit():
            print("please put a numeric value")
        else:
            settings["maintenanceCost"] = int(maintenanceCostInput)
            break

    while True:
        trainPriceInput = input(
            f"""maintenance cost 
default: {settings["trainPrice"]} money
leave empty for default
"""
        )
        if not trainPriceInput:
            print("using default")
            break
        if not str(trainPriceInput).isdigit():
            print("please put a numeric value")
        else:
            settings["trainPrice"] = int(trainPriceInput)
            break

    while True:
        carPriceInput = input(
            f"""maintenance cost 
default: {settings["carPrice"]} money
leave empty for default
"""
        )
        if not carPriceInput:
            print("using default")
            break
        if not str(carPriceInput).isdigit():
            print("please put a numeric value")
        else:
            settings["carPrice"] = int(carPriceInput)
            break

    while True:
        startingMoneyInput = input(
            f"""starting money
default: {settings["startingMoney"]} money
leave empty for default
"""
        )
        if not startingMoneyInput:
            print("using default")
            break
        if not str(startingMoneyInput).isdigit():
            print("please put a numeric value")
        else:
            settings["startingMoney"] = int(startingMoneyInput)
            break

    return settings