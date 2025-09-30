def input_validation(inp) -> bool:
    for c in inp:
        if c.isdigit() or c.isalpha():
            continue
        else:
            return False
    return True


def main_menu_input_handler(inp) -> str:
    inp = inp.lower()
    if not input_validation(inp):
        main_menu_input_handler(
            input("please dont use any spaces or special charcters\n")
        )
    match inp:
        case "q":
            print("quiting\n")
            return "q"
        case "0" | "help":
            return "help"
        case "1" | "city":
            return "city"
        case "2" | "station":
            return "station"
        case "3" | "train":
            return "train"
        case "4" | "route":
            return "route"
        case _:
            inp = main_menu_input_handler(input
                                          ("please pick on of our optiions\n")
                                          )
            return inp


def main():
    while True:
        test = main_menu_input_handler(input("pick a input\n"))
        if test == "q":
            break


main()
