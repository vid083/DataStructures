import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

    #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")
        print(lives)

    print(f"{' '.join(display)}")

    if "_" not in display:
      end_of_game = True
      print("You win.")

    
print(stages[lives])