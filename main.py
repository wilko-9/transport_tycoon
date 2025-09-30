def input_validation(inp) -> bool:
    return True


def main_menu_input_handler(inp):
    inp = inp.lower()
    if not input_validation(inp):
        main_menu_input_handler(
            input("please dont use any spaces or special charcters")
        )
    match inp:
        case "q":
            print("quiting")
            return "q"
        case _:
            main_menu_input_handler(input
                                    ("please pick on of our optiions")
                                    )


def main():
    while True:
        test = main_menu_input_handler(input("pick a input"))
        if test == "q":
            break


main()
