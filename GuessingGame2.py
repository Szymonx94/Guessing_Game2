def guessing():
    """
    Main function for our program uses users answers to find a number in range (1, 1000) imagined
    by the user.
    :param: string
    """
    min = 0
    max = 1000
    guess = int((max - min) / 2) + min
    print(f"My guess is: {guess}")

    answer = ["Too small", "Too big", "You win"]
    user_answers = input("Is that a good number? ")
    i = 0

    while i < 10:
            if user_answers not in answer:
                print("Your answer is wrong!")
                user_answers = input("Is that a good number? ")
            elif user_answers == "You won":
                print(" I won")
                break
            elif user_answers == "Too small":
                min = guess
                guess = int((max - min) / 2) + min
                print(f"My guess is: {guess}")
                user_answers = input("Is that a good number? ")
                i += 1
            elif user_answers == "Too big":
                max = guess
                guess = int((max - min) / 2) + min
                print(f"My guess is: {guess}")
                user_answers = input("Is that a good number? ")
                i += 1

            if i == 10 and user_answers != answer[2]:
                print("You are cheating a lot of the answers")
                print(f"My guess is: {guess}")
                i += 1

if __name__ == '__main__':
    guessing()
