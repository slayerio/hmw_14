import random


def check_guess(lucky_number: int, user_guess: str) -> str:
    number = int(user_guess)

    if number < 0:
        raise ValueError("Number is negative")
    if number > 100:
        raise ValueError("Number out of range")

    if number == lucky_number:
        return "BINGO!"
    elif number > lucky_number:
        return "lower"
    else:
        return "higher"


def game_guessing_play():
    while True:
        lucky_number = random.randint(0, 100)
        while True:
            try:
                user_guess = input("Guess a number between 0-100: ")
                result = check_guess(lucky_number, user_guess)
                print(result)
                if result == "BINGO!":
                    break
            except ValueError as e:
                print(e)
        while True:
            play_again = input("Want to play again? (yes/no): ").lower()
            if play_again == "no":
                print("thanks for playing!")
                return
            elif play_again == "yes":
                break
            else:
                print("Invalid response, only 'yes' or 'no' are allowed.")
        return


if __name__ == "__main__":
    game_guessing_play()



