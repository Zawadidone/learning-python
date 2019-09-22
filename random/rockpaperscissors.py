# import modules
import random
import time

# dictionary with choices
lists = {
    1: "rock",
    2: "paper",
    3: "scissors",
}


def main():
    print("Welcome are you ready to play rock-paper-scissors")  # the user gets to chose his element
    user_choice = choice_user()
    computer_choice = choice_computer()
    print(rps(user_choice, computer_choice))


def choice_user():  # Choose a element when input is not equal to 1-3 it gives a error and repeats the function
        try:
            for n, e in lists.items():
                print(n, e)
            element = int(input())
            if element in (1, 2, 3):  # if element is between 1 and 3 the function returns the element
                return lists[element]
            else:
                print("Choose a number between 1 and 3!")
                time.sleep(1)
                return choice_user()
        except ValueError:
            print("No valid number! Please try again ...")
            return choice_user()


def choice_computer():
    choice = random.randint(1, 3)
    return lists[choice]


def rps(user, computer):  # function algorithm rock-paper-scissors
    print("User:", user)
    print("Computer:", computer)
    if user == computer:
        return "It's a tie"
    elif user == "rock":
        if computer == "scissors":
            return "User wins"
        else:
            return "Computer wins"
    elif user == "paper":
        if computer == "rock":
            return "User wins"
        else:
            return "Computer wins"
    elif user == "scissors":
        if computer == "rock":
            return "Computer wins"
        else:
            return "User wins"
    else:
        return "Not possible"

if __name__ == '__main__':
    main()
