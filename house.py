name = input("What's your name? ")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Griffindor")
    case _:
        print("Who?")