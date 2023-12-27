import random
from hangman_art import stages, logo
stages = stages[::-1]

end_of_game = False
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(logo)

#print(f'The solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
      print("You've already guessed this letter, try again.")
    else:
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

      if guess not in chosen_word:
        lives -= 1
      if lives == 0:
        print(f"You lose.\nThe word was: {chosen_word}")
        print(stages[lives])
        break

      print(f"{' '.join(display)}")

      if "_" not in display:
          end_of_game = True
          print("You win!")

      print(stages[lives])

      guessed_letters.append(guess)