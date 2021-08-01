# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from art import logo
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
scores = {"user": 0, "computer": 0}


def get_rand_index():
    return random.randint(0, len(deck) - 1)


def serve_cards(user_cards, computer_cards):
    user_cards.append(deck[get_rand_index()])
    user_cards.append(deck[get_rand_index()])
    computer_cards.append(deck[get_rand_index()])
    computer_cards.append(deck[get_rand_index()])

def hit(cards):
    cards.append(deck[get_rand_index()])

def get_sum(cards: []):
    sum = 0
    for i in range(len(cards)):
        sum += cards[i]
    return sum


def do_computer_hit_if_needed(computer_cards):
    if get_sum(computer_cards) <= 12:
        hit(computer_cards)


def increment_score(user):
    scores[user] += 1


def decide_winner(user_cards, computer_cards):
    user_score = get_sum(user_cards)
    computer_score = get_sum(computer_cards)

    if user_score <= 21 and user_score > computer_score:
        print("You Won!")
        increment_score('user')
    elif computer_score <= 21 and computer_score > user_score:
        print("Computer Won!")
        increment_score('computer')
    else:
        print("Draw!")




def main():
    print(logo)  # Press ⌘F8 to toggle the breakpoint.
    print("Welcome to the black jack game!")
    user_cards = []
    computer_cards = []
    repeat = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    while repeat.lower() != 'n' and repeat.lower() == 'y':
        serve_cards(user_cards, computer_cards)
        print("User: ", user_cards)
        print("Computer: ", [computer_cards[random.randint(0, 1)]])

        do_hit = input("Do you want to hit another card? Type 'y' or 'n'")

        if do_hit.lower() == 'y':
            hit(user_cards)

        do_computer_hit_if_needed(computer_cards)

        decide_winner(user_cards, computer_cards)
        print("User: ", user_cards)
        print("Computer: ", computer_cards)
        print(f'Current score: {scores}')

        user_cards = []
        computer_cards = []
        repeat = input("Do you want to continue playing? 'y' or 'n': ")


if __name__ == '__main__':
    main()
