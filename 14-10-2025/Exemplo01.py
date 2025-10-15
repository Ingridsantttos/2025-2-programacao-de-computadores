'''
   Escreva um programa que pede ao usuário para inserir um ano e 
   determina se ele é bissexto ou não. 
   
   Um ano é bissexto se atender a uma das seguintes regras:

      - É divisível por 4, mas não é divisível por 100.

      - É divisível por 400.

      (Por exemplo, 2000 e 2400 são bissextos; 1800, 1900 e 2100 não são). 
      
   O programa deve exibir "O ano [ano] é bissexto." ou 
   "O ano [ano] não é bissexto.". 
   
   Use try...except para validar a entrada.
'''
from ast import Try

Try

ano = int(input("Digite um ano: "))
# verifica se é bissexto 
"if (ano % 4 == 0 and ano % 100 != 0) or ( ano % 400 == 0)"
print (f"0 ano {ano} é bissexto.")
"else"
print(f"0 o ano {ano} não é bissexto.")
"except ValueError"
print("entrada inválida! por favor, digite um número inteiro")




