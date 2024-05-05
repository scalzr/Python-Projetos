import random

user_wins = 0
computer_wins = 0

options = ["pedra", "papel", "tesoura"]

while True:
    user_input = input("Escolha Pedra/Papel/Tesoura ou S para sair: ").lower()
    if user_input == "s":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # pedra: 0, papel: 1, tesoura: 2
    computer_pick = options[random_number]
    print("Maquina escolheu", computer_pick + ".")

    if user_input == "pedra" and computer_pick == "tesoura":
        print("Ganhou!")
        user_wins += 1

    elif user_input == "papel" and computer_pick == "pedra":
        print("Ganhou!")
        user_wins += 1

    elif user_input == "tesoura" and computer_pick == "papel":
        print("Ganhou!")
        user_wins += 1

    else:
        print("Perdeu! ")
        computer_wins += 1
    
print("Ganhou!", user_wins, "times.")
print("Perdeu!", computer_wins, "times.")
print("Até!")
