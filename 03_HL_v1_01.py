import math
import random


# instruction if user did not play the game before


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print("For each game you will be asked to...")
    print("- Enter a 'low' and 'high' number. "
          "The computer will randomly generate a 'secret' number between your two chosen numbers."
          " It will use these numbers for for all the rounds in a given game.")
    print("- The computer will calculate how many guesses you are allowed")
    print("- enter the number of rounds you want to play")
    print("- guess the secret number")
    print()
    print("Good Luck!")


# decorating program to decorate the game


# yes or no answer for the program
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please enter yes or no")


def statement_generator(outcome, prize_decoration):

    sides = prize_decoration * 3

    outcome = "{} {} {}".format(sides, outcome, sides)
    top_bottom = prize_decoration * len(outcome)

    print(top_bottom)
    print(outcome)
    print(top_bottom)

    return ""


def start():
    print()
    print("lets get started")
    print()
    prize_decoration = "-"
    return""


def int_check(question, low=None, high=None):

    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # check input is not too high or
            # too low if a both upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("please enter a number between "
                          "{} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more "
                          "than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is a integer
        except ValueError:
            print("Please enter an integer")
            continue

# introduction for the game
# ask if they have played this game before
# if no show instructions
# if yes continue

statement_generator("Welcome to Higher or lower", "*")
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

if played_before == "yes":
    start()


# ask user for # of rounds then loop...

game_summary = []

rounds_lost = 0
rounds_drawn = 0
rounds_played = 0


lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)

num_range = highest - lowest + 1
max_raw = math.log2(num_range)  # finds maximum # of guesses using
max_upped = math.ceil(max_raw)  # rounds up (ceil ---> ceiling)
max_guesses = max_upped + 1
print("Max Guesses: {}".format(max_guesses))


while rounds_played < rounds:
    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    # HL component 11 - Maximum Guesses Calculator

    secret = random.randint(lowest, highest)
    GUESSES_ALLOWED = 5

    # list for guesses
    already_guessed = []
    guesses_left = GUESSES_ALLOWED
    num_won = 0

    guess = ""

    while guess != secret and guesses_left >= 1:

        guess = int(input("Guess: "))  # replace this with function

        # check that guess is not a duplicate

        if guess in already_guessed:
            print("You already guessed that number! Please try again"
                  "you *still* have {} guesses left".format(guesses_left))
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:

            if guess < secret:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

            elif guess > secret:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
        else:
            if guess < secret:
                print("Too Low!")
            elif guess > secret:
                print("Too High!")

    if guess == secret:
        if guesses_left == GUESSES_ALLOWED -1:
            print("Amazing! You got it")
        elif guess == secret:
            print("Well done, you got it")

if guess and rounds_played:
    round_result = "won"
if guess and rounds_played:
    round_result = "lost"

game_summary.append(round_result)

round_result = "Round {}: {}".format(rounds_played + 1, round_result)

# Ask user if they want to see their game history.
# If 'yes' show game game history

# Show game statistics
rounds_won = rounds_played - rounds_lost - rounds_drawn

# **** Calculate Game Stats ****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()

# display game stats with % values to the nearest whole number
print("******* Game statistics *******")
print("Win: {}, ({:.0f}%)\nLoss: {}, "
      "({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won,
                                             percent_win,
                                             rounds_lost,
                                             percent_lose,
                                             rounds_drawn,
                                             percent_tie))
print()
print("Thanks for playing")
