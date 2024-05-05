MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("Quanto será depositado? R$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Precisa ser maior que 0.")
        else:
            print("Digite um numero: ")

        return amount

def get_number_of_lines():
    while True:
        lines = input("Digite o numero de linhas que irá apostar (1- " +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Digite um numero valido de linhas.")
        else:
            print("Digite um numero.")

    return lines

def get_bet():
    while True:
        amount = input("Quanto será apostado em cada linha? R$ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"A quantia deve ser entre R${MIN_BET} - R${MAX_BET}.")
        else:
            print("Digite um numero: ")

        return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"Está apostando R${bet} em {lines} linhas. Aposta total é igual a: R${total_bet}")

main()
            

    
