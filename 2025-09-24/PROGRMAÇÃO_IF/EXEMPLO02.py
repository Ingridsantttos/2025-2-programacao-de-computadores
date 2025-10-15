'''
   Desenvolva um programa que calcula o IMC de uma pessoa. 
   
   O programa deve pedir o peso em quilogramas (ex: 70.5) e a 
   altura em metros (ex: 1.75). 
   
   A fórmula do IMC é: peso / (altura * altura). 
   
   Após calcular o IMC, o programa deve exibir o valor e a 
   classificação correspondente, de acordo com a tabela:

      - Abaixo de 18.5: Abaixo do peso
      - 18.5 a 24.9: Peso ideal
      - 25.0 a 29.9: Sobrepeso
      - 30.0 a 34.9: Obesidade Grau I
      - Acima de 35.0: Obesidade Grau II

   O programa deve tratar entradas inválidas (não numéricas) e 
   também verificar se a altura informada é maior que zero para evitar 
   um erro de divisão.      
'''
 
from unittest import expectedFailure


Peso = float(input("digite o peso em kg: "))
altura = float(input("digite a altura em metros: "))
if altura<= 0:
 print("a altura deve ser maior que zero.")
else:
 imc = "peso" / (altura *  altura)
 print(f"nseu IMC é: {imc: .2f}")
 if imc < 18.5:
  print("classificação: abaixo peso")  
if imc < 25:
  print("classificação: peso ideal")  
elif imc < 30:
   print("classificação: sobrepeso")
elif imc < 35:
   print("classificação: obesidade grau I")
else:
   print("classificação: obesidade grau II")
"except ValueError"
print("entrada inválida. Digite valores numéricos")
