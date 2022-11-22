import random
from hangman_images import stages , logo
from hangman_words import word_list
print(logo)
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
lives=6
count=0
print(f"Psst, the solution if {chosen_word}.")
display=[]
for _ in range(word_length):
    display.append("_")
print(display)
end_of_game=False
while  end_of_game==False:
    guess=input("Guess a letter: ").lower()
    if guess in display:
      count+=1
      print(f"You've already guessed '{guess}' {count} times.")
    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    print(display)
    if guess not in chosen_word:
      print(f"You guess {guess}, that's not in the word. You lose a life. ")
      lives-=1
      print(stages[lives])
      if lives==0:
        end_of_game=True
        print("You loose")

    if "_" not  in display:
      end_of_game=True
      print('You win')
  