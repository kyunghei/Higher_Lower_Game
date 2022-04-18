import random
from Game_Data import data
from art import logo, vs

def two_random():
    """Randomly chooses two unique samples from data set"""
    return random.sample(data, 2)


def user_choice():
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return guess


def win_or_lose(guess):
    if guess == "A" and choice_a["follower_count"] > choice_b["follower_count"]:
        print("You\'re right!")
        return win_counter + 1
    elif guess == "B" and choice_b["follower_count"] > choice_a["follower_count"]:
        print("You\'re right!")
        return win_counter + 1
    else:
        print("\nYou lose.")
        print(f"Your final score is {win_counter}.")
        exit()


choice_a = two_random()[0]
choice_b = two_random()[1]

win_counter = 0
keep_playing = True

while keep_playing == True:
    print(logo)
    print(f"\nCompare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
    win_counter = win_or_lose(user_choice())

    choice_a = data[data.index(choice_b)]
    new_index = random.randint(0,49)
    while random.randint(0,50) == data.index(choice_a):
        new_index = random.randint(0,49)
    choice_b = data[new_index]
    print(f"Your current score is {win_counter}.")

