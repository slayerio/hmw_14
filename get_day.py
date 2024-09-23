
def check_number(day: int) -> str:
    if day > 7:
        raise ValueError("number is out of range")
    if day < 1:
        raise ValueError("number cannot be zero or negative")
    match day:
        case 1:
            return "sunday"
        case 2:
            return "monday"
        case 3:
            return "tuesday"
        case 4:
            return "wednesday"
        case 5:
            return "thursday"
        case 6:
            return "friday"
        case 7:
            return "saturday"

def game_guessing_play():
    while True:
            try:
                user_num = int(input("Guess a day of the week (1-7)"))
                result = check_number(user_num)
                print(result)
                break
            except ValueError as e:
                print(e)

    while True:
        play_again = input("Want another shot? (yes/no): ").lower()
        if play_again == "no":
            print("thanks!")
            return
        elif play_again == "yes":
            break
        else:
            print("Invalid response, only 'yes' or 'no' are allowed.")
    return


if __name__ == "__main__":
    game_guessing_play()



