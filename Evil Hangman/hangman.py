#Xavier Goudeaux
from ctypes.wintypes import WORD



class Hangman:

  	#initializes the length of the word, the maz amount of guesses, and the remaining words
    #to be input later on in other methods	  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    def __init__(self,word_length = None ,guesses = None,remaining_words = []):
        self.word_length = word_length
        self.guesses = guesses
        self.remaining_words = remaining_words

    #reads the dictionary.txt file line by line (or another test file with different words)
    def dictionary_reader(self,dictionary):
        with open(str(dictionary)) as file:
            for line in file:
                if len(line.strip()) == self.word_length:
                    self.remaining_words.append(line.strip())
        
    #returns the amount of guesses the user has left
    def get_guesses(self):
        return "Guesses left: " + str(self.guesses)

    #returns the words the computer has left to trick the player with
    def get_remaining_words(self):
        return self.remaining_words
    
    #returns the amount of words left in the computer
    def word_count(self):
        return "Words left: " + str(len(self.remaining_words))

    #initializes a '-' pattern based on the amount of letters input by the user
    def init_pattern(self,word_length):
        blanks = ""
        for i in range(word_length):
            blanks += '_'
        return blanks

    #resets the remaining_words set
    def list_reset(self):
        self.remaining_words = []

    #creates word families based on the letter guessed by the user, the remaining words,and the pattern currently under review
    def word_families(self,remaining_words,guess_letter,origin_pattern):
        families = {}
        for word in remaining_words:
            pattern = ""
            for i in range(len(word)):
                if word[i] == guess_letter:
                    pattern += guess_letter
                elif word[i] == origin_pattern[i]:
                    pattern += word[i]
                else:
                    pattern += '_'

            if pattern not in families:
                families[pattern] = []
            families[pattern].append(word)

        return families
                
           
    #returns a new pattern based on which pattern has the largest amount of words 
    def pattern_generator(self,families):

        max_pattern = 0 
        for pattern in families:
            if len(families[pattern]) > max_pattern:
                max_pattern = len(families[pattern])


            evil_pattern = ""  

        for pattern in families:
            if len(families[pattern]) == max_pattern:
                evil_pattern = pattern
                break


        self.remaining_words = families[evil_pattern]

        return evil_pattern

           
        



    def play(self):

        print("===Welcome to Evil Hangman===")
        
        #at beginning: prompt for word length,number of guesses,see list of remaining words(?)
        self.word_length = input("How many letters should the word have?: ")
        while self.word_length.isdigit() == False:
            print("Please enter a NUMBER")
            self.word_length = input("How many letters should the word have?: ")
        self.word_length = int(self.word_length)

        self.guesses = input("How many guesses do you want?: ")
        while self.guesses.isdigit() == False:
            print("Please enter a NUMBER")
            self.guesses = input("How many guesses do you want?: ")
        self.guesses = int(self.guesses)
            

        show = input("Would you like to see the remaining words?(yes/no): ")
        while show.isdigit() == True:
            print("This response is invalid")
            show = input("Would you like to see the remaining words?(yes/no): ")
        print()
        
        #reads dicitonary.txt and puts all of the words into a set of remaining words
        self.dictionary_reader('dictionary.txt')

        #pattern visiual for user to track progress in game
        word_box = str(self.init_pattern(self.word_length))
        letter_box = []
        
        #game runs until user runs out of guesses (or wins!)
        while self.guesses > 0:

            if show == "yes":
                print(self.get_remaining_words())
                print(self.word_count())
                print()
            
            print("Letter box: " , letter_box)
            print(word_box+"\n")
            print(self.get_guesses())
            

            guess_letter = input("Guess a letter: ")
            while guess_letter.isalpha() == False or len(guess_letter) > 1:
                print("This input is invalid.")
                guess_letter = input("Guess a letter: ")
            print()
            

            if guess_letter not in letter_box:
                letter_box.append(guess_letter)
            else:
                print("You have already guessed that letter. Try again.")
                continue
            
            word_box = self.pattern_generator(self.word_families(self.remaining_words, guess_letter, word_box))

            if guess_letter not in word_box:
                self.guesses -= 1
                continue
    
            if word_box == self.remaining_words[0]:
                print("CONGRATULATIONS! YOU WON!")
                print("The word was" , self.remaining_words[0] + ".")
                self.list_reset()
                print()
                break

        if self.guesses == 0:
            print("You have run out of guesses.")
            print("The word was" , self.remaining_words[0] + ".\nGame Over\n")
            self.list_reset()

                

      

            

            
           
            


            
       

            

                
                        

                    



            

            

    
        



    

               