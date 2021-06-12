
secret_word = "giraffe"

guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_count += 1
        guess = input("guess the secret: ")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("you lost")
else:
    print("you win after "+str(guess_count)+" attempt(s)!")


