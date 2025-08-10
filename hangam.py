import random

WORDS = ["python", "database", "autoencoder", "analysis", "university", "algorithm", "network"]

def choose_word():
    return random.choice(WORDS).lower()

def display_state(secret, guessed):
    display = " ".join([c if c in guessed else "_" for c in secret])
    print("\nWord: ", display)

def hangman():
    secret = choose_word()
    guessed = set()
    wrong_guesses = set()
    max_wrong = 6

    print("Welcome to Hangman!")
    while True:
        display_state(secret, guessed)
        print(f"Wrong guesses ({len(wrong_guesses)}/{max_wrong}):", " ".join(sorted(wrong_guesses)))
        if all(c in guessed for c in secret):
            print("\n🎉 You guessed the word:", secret)
            break
        if len(wrong_guesses) >= max_wrong:
            print("\n💥 You lost. The word was:", secret)
            break

        guess = input("Enter a letter (or full word): ").strip().lower()
        if not guess:
            continue
        if len(guess) == 1:
            if guess in guessed or guess in wrong_guesses:
                print("Already tried", guess)
                continue
            if guess in secret:
                guessed.add(guess)
                print("Correct!")
            else:
                wrong_guesses.add(guess)
                print("Wrong!")
        else:
            # player guessed whole word
            if guess == secret:
                print("\n🎉 Correct! You guessed the whole word:", secret)
                break
            else:
                print("That's not the word.")
                wrong_guesses.add(guess[0])  # penalize slightly

if '_name_' == "_main_":
    hangman()
