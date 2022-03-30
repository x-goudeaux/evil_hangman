from hangman import Hangman

# Create an instance of hangman
game = Hangman()
# Call play method that begins and plays the game
game.play()
# Game is over. Ask if user would like to play again.
y = input("Would you like to play again? yes or no: ")
# Continuously play and ask user to play again.
while y == 'yes':
    game.play()
    y = input("Would you like to play again? yes or no: ")