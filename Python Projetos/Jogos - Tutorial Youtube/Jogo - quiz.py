#Início

print("Bem vindo ao SZ Quiz!! ")

playing = input ("Gostaria de jogar? ")

if playing != "sim":
    quit()

print("Beleza! Vamos para o Quiz :) ")
score = 0

#Pergunta 01

answer = input("Qual o nome do estado Brasileiro que o Matheus vive? ")
if answer.lower() == "rio de janeiro" or answer == "rj" or answer == "rio":
    print('Acertou!')
    score += 1

else:
    print("Errou! Matheus mora no Rio de Janeiro.")

#Pergunta 02

answer = input("Para qual time de futebol Matheus torce? ")
if answer.lower() == "vasco" or answer == "vasco da gama":
    print('Acertou!')
    score += 1

else:
    print("Errou! Matheus torce pro Vasco.")

#Pergunta 03

answer = input("Qual a bebida não alcólica favorita de Matheus? ")
if answer.lower() == "mate" or answer == "mate leão" or answer == "mate limão" or answer == "mate leão limão" or answer == "mate leão com limão":
    print('Acertou!')
    score += 1

else:
    print("Errou! Matheus ama Mate Leão Limão.")

#Pergunta 04

answer = input("Quantos anos tem Matheus? ")
if answer.lower() == "21" or answer == "vinte e um" or answer == "vinte e um":
    print('Acertou!')
    score += 1

else:
    print("Errou! Matheus tem 21 anos.")

#Pergunta 05

answer = input("Qual o nome da faculdade que Matheus Estuda? ")
if answer.lower() == "estácio" or answer == "estacio" or answer == "estacio de sa" or answer == "estácio de sá":
    print('Acertou!')
    score += 1

else:
    print("Errou! Matheus estuda na Estácio.")

#Resultado
    
print("Adquiris-te " +str(score) + " Respostas Corretas!")
print("Adquiris-te " +str((score/5) * 100) + "% de Respostas Corretas!")

