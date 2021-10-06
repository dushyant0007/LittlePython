import random
import logo


print(logo.logo)

wordList = ["dog", "jaipur", "classroom"]
choseWorld = random.choice(wordList)
display = []

for i in range(0, len(choseWorld)):
    display.append('_')

print(display)

endOfGame = False
lives = 6
while not endOfGame:

    guess = input("Guess the letter")
    if guess in display:
        print(f"You've already guess {guess}")
    for position in range(0, len(choseWorld)):
        letter = choseWorld[position]
        if letter == guess:
            display[position] = guess
        # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if guess not in choseWorld:
        print(f"You guessed {guess}, that's not in the world. You lose a life ")
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You Loose")

    print(display)

    if "_" not in display:
        endOfGame = True
        print("You Win")

    print(logo.stages[lives])
