
import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class BlackJack:
    def __init__(self):
        self._player_cards = []
        self._player_score = 0
        self._computer_score = 0
        self._computer_cards = []

    # Calculating the sum of all the cards in the list
    def calculate_score(self, card: list) -> int:
        score = 0
        for i in range(len(card)):
            score += card[i]
        return score
    
    def generate_cards(self):
        random_cards = []
        random_cards = [random.choice(cards) for i in range(2)]
        if random_cards[0] == 11 and random_cards[1] == 11:
            random_cards[1] = 1
        return random_cards
    
    def ace_value(self, current_score, card):
        if card == 11 and (card + current_score) > 21:
            return 1
        else:
            return card
        
    # Printing the final score and sets of cards for both player
    def display_scores(self):
        print(f"Your final hand {self._player_cards}, final score: {self._player_score}")
        print(f"Computer's final hand: {self._computer_cards}, final score: {self._computer_score}")

    # Printing congratulatory or losing message
    def compare_scores(self):
        if self._player_score > 21:
            print(f"You went over. You lose 😭")
        elif self._player_score == self._computer_score:
            print("Draw 🙃")
        elif self._computer_score > 21:
            print(f"Opponent went over. You win 😭")
        elif self._player_score < self._computer_score:
            print("You lose 😤")
        else:
            print("You win 😁")

    # Resetting scores to zero and cards to empty
    def reset(self):
        self._player_cards = []
        self._player_score = 0
        self._computer_score = 0
        self._computer_cards = []
        
    def display_logo(self):
        print(f"\n" * 30)
        print(art.logo)

    # Games' logic
    def play_game(self):

        self.display_logo()

        # initial player's 2 cards
        self._player_cards = self.generate_cards()
        
        # initial player's score
        self._player_score = self.calculate_score(self._player_cards)

        # initial computer's 2 cards
        self._computer_cards = self.generate_cards()

        # initial computer's score
        self._computer_score = self.calculate_score(self._computer_cards)
        while self._computer_score < 17:
            new_comp_card = self.ace_value(self._computer_score, random.choice(cards))
            self._computer_cards.append(new_comp_card)
            self._computer_score = self.calculate_score(self._computer_cards)

        is_continue = True
        while is_continue:
            print(f"Your cards {self._player_cards}, current score: {self._player_score}")
            print(f"Computer's first card: {self._computer_cards[0]}")
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
            if user_choice == "y":
                new_player_card = self.ace_value(self._player_score, random.choice(cards))
                self._player_cards.append(new_player_card)
                self._player_score = self.calculate_score(self._player_cards)
                if self._player_score > 21:
                    is_continue = False
            elif user_choice == "n":
                is_continue = False

            else:
                print("Invalid input")

        self.display_scores()
        self.compare_scores()

# Main Function
def main():
    bj = BlackJack()
    while True:
        bj.reset()
        user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
        if user_input == "y":
            bj.play_game()
        elif user_input == "n":
            break
        else:
            print("Invalid input")

if __name__=="__main__":
    main()