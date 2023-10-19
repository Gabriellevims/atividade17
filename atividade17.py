# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
import time 
print("alistamento ")

ano= int(input("Digite seu ano de nascimento:"))
x= time.localtime ()
idade = (x[0]-ano)
if idade > 18:
    print(f"você ja passou da idade certa pra se alista, passou se {idade-18} anos.")
elif idade == 18:
    print("você esta na idade certa pra se alistar.")
else:
    print(f"você não esta na idade certa para se alistar, espere {18-idade}anos.")