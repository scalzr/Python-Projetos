import random

top_of_range = input("Digite um numero: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Digite um numero maior que 0 na proxima vez.')
        quit()

else:
    print('Digite um numero na proxima.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("De um palpite: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('Digite um numero na proxima.')
        continue
    if user_guess == random_number:
        print("Acertou! ")
        break
    else:
        if user_guess > random_number:
            print("Menos! ")
        else:
            print("Mais! ")

print("Acertou em", guesses, "palpites. ")

