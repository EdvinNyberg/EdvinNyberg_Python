import random  # Import the random module to generate random numbers

# Class to represent a player in the card game
class Player:
    def __init__(self, name: str): # Constructor to initialize the player's name and score

        self.name: str = name
        self.score: int = 0

    def draw_card(self) -> int:
        """
        Draw a card with a value between 1 and 13. If the card is an Ace (value 1),
        handle it specially by allowing the player to choose its value or setting it
        based on the house's strategy.
        
        """
        card: int = random.randint(1, 13)  # Draw a random card with a value between 1 and 13
        
        if card == 1:  # If the card is an Ace
            if self.name == "Player":
                # Ask the player if they want the Ace to be worth 14 or 1
                ace_value = 14 if input("You drew an Ace! Do you want it to be 14? (y/n): ").lower() == 'y' else 1
                print(f"Your ace is worth {ace_value}.")
                return ace_value
            else:
                # For the House, Ace is worth 14 only if it doesn't cause a bust
                ace_value = 14 if self.score + 14 <= 21 else 1
                print(f"The House drew an Ace! It is worth {ace_value}.")
                return ace_value
        
        print(f"{self.name} drew a {card}!")  # Give feedback on the drawn card
        return card

    def play_turn(self) -> bool:
        """
        Allow the player to draw cards until they decide to stop or bust.
        
        """
        while True: # Loop to allow the player to draw cards
            self.score += self.draw_card()  # Add the drawn card value to the player's score
            print(f"{self.name}'s current score: {self.score}")  # Print the current score
            
            if self.score > 21:  # Check if the player has busted
                print(f"{self.name} busted! {'House wins.' if self.name == 'Player' else 'You win.'}")
                return False  # Return False if the player busts
            
            if self.name == "Player":
                # Ask the player if they want to draw another card
                if input("Do you want to draw another card? (y/n): ").lower() != 'y':
                    break  # Player decides to stop drawing cards
            
            if self.name == "House" and self.score >= 16:
                break  # House stops drawing cards if score is 16 or more
        
        return True  # Return True if the player didn't bust


class CardGame: # Class to represent the card game
    def __init__(self):
        self.player = Player("Player")
        self.house = Player("House")

    def play_game(self):
        print("Welcome to Cosmopol! This is the table for the card game twenty-one.")
        print("Rules: Try to get as close to 21 as possible without going over. Aces can be worth 1 or 14.")
        first_game = True
        while True: # Loop to allow the player to play multiple rounds
            if first_game:
                print("Would you like to play? (yes/no)")
                first_game = False  # Set first_game to False to skip this block in the next iteration
            else: # Ask the user if they want to play again
                print("\nWould you like to play again? (yes/no)")

            response: str = input().strip().lower()  # Get the user's response and convert it to lowercase

            if response == 'yes':  # Start the game if the user wants to play
                print("Great! Let's start the game.")
                self.player.score = 0  # Reset player's score for a new game
                self.house.score = 0  # Reset house's score for a new game
            elif response == 'no':  # End the game if the user doesn't want to play
                print("Alright, maybe next time. Goodbye!")
                return # Exit the function to end the game
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")
                continue

            if not self.player.play_turn():  # Player's turn - if the player busts, end the game
                continue
            if not self.house.play_turn():  # House's turn - if the house busts, end the game
                continue
            if self.player.score > self.house.score:  # Compare the scores to determine the winner
                print(f"\nYou win! Your score: {self.player.score}, House score: {self.house.score}")
            elif self.player.score == self.house.score:
                print(f"\nIt's a draw! House wins. Your score: {self.player.score}, House score: {self.house.score}")
            else:
                print(f"\nHouse wins! Your score: {self.player.score}, House score: {self.house.score}")

            print("\n----------------------------------------")

if __name__ == "__main__":
    # Create an instance of CardGame and start the game
    game = CardGame()  # An instance of the CardGame class representing the card game
    game.play_game()  # Start the card game