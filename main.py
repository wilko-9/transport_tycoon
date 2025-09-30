def input_validation(inp) -> bool:
    for c in inp:
        if c.isdigit() or c.isalpha():
            continue
        else:
            return False
    return True


def main_menu_input_handler(inp):
    inp = inp.lower()
    if not input_validation(inp):
        main_menu_input_handler(
            input("please dont use any spaces or special charcters\n")
        )
    match inp:
        case "q":
            print("quiting\n")
            return "q"
        case _:
            main_menu_input_handler(input
                                    ("please pick on of our optiions\n")
                                    )


def main():
    while True:
        test = main_menu_input_handler(input("pick a input\n"))
        if test == "q":
            break


main()
