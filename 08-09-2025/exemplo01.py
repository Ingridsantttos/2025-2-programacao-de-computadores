'''

   Faça um programa que solicite ao usuário um número de até 4 dígitos inteiro positivo e exiba a soma dos seus algarismos.

   Exemplo: 2456 = 17 (2 + 4 + 5 + 6)

   DICA: Vocês irão usar o operador de divisão inteira (//) e o operador de resto de divisão inteiro (%)

'''

numero = int(input("digite um numero"))

soma = 0

while numero > 0:
    soma += numero % 10 # pega o ultomo digito
    numero = numero // 10 #remove p ultimo digito

    # exibe o resultado 

    print("A soma do algarismo é:",soma)