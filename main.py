

# 11 and 1 concern

import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class BlackJack:
    def __init__(self):
        self.player_cards = []
        self.player_score = 0
        self.computer_score = 0
        self.computer_cards = []

    # Calculating the sum of all the cards in the list
    def calculate_score(self, card: list) -> int:
        score = 0
        for i in range(len(card)):
            score += card[i]
        return score

    # Games' logic
    def play_game(self):
        print(f"\n" * 20)
        print(art.logo)

        # initial player's 2 cards
        self.player_cards = [random.choice(cards) for i in range(2)]
        if self.player_cards[0] == 11 and self.player_cards[1] == 11:
            self.player_cards[1] = 1

        # initial player's score
        self.player_score = self.calculate_score(self.player_cards)

        # initial computer's 2 cards
        self.computer_cards = [random.choice(cards) for i in range(2)]
        if self.computer_cards[0] == 11 and self.computer_cards[1] == 11:
            self.computer_cards[1] = 1

        # initial computer's score
        self.computer_score = self.calculate_score(self.computer_cards)

        while self.computer_score < 17:
            new_comp_card = random.choice(cards)
            if new_comp_card == 11 and (new_comp_card + self.computer_score) > 21:
                new_comp_card = 1
            self.computer_cards.append(new_comp_card)
            self.computer_score += new_comp_card

        is_continue = True
        while is_continue:
            print(f"Your cards {self.player_cards}, current score: {self.player_score}")
            print(f"Computer's first card: {self.computer_cards[0]}")
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
            if user_choice == "y":
                new_player_card = random.choice(cards)
                if new_player_card == 11 and (new_player_card + self.player_score) > 21:
                    new_player_card = 1
                self.player_cards.append(new_player_card)
                self.player_score += new_player_card
                if self.player_score > 21:
                    is_continue = False
            elif user_choice == "n":
                is_continue = False

            else:
                print("Invalid input")

        # Printing the final score and sets of cards for both player
        print(f"Your final hand {self.player_cards}, final score: {self.player_score}")
        print(f"Computer's final hand: {self.computer_cards}, final score: {self.computer_score}")

        # Printing congratulatory or losing message
        if self.player_score > 21:
            print(f"You went over. You lose 😭")
        elif self.player_score == self.computer_score:
            print("Draw 🙃")
        elif self.computer_score > 21:
            print(f"Opponent went over. You win 😭")
        elif self.player_score < self.computer_score:
            print("You lose 😤")
        else:
            print("You win 😁")

# Main Function
def main():
    bj = BlackJack()
    while True:
        user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
        if user_input == "y":
            bj.play_game()
        elif user_input == "n":
            break
        else:
            print("Invalid input")

if __name__=="__main__":
    main()