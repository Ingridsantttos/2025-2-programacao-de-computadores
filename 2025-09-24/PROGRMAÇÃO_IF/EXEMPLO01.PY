'''
   Crie um programa que calcula o salário semanal de um funcionário.
   
   O programa deve solicitar o número de horas trabalhadas na semana e o 
   valor que ele recebe por hora. A jornada de trabalho padrão é de 40 horas 
   semanais. Horas trabalhadas acima de 40 devem ser pagas com um adicional 
   de 50% (o valor da hora extra é 1.5 vezes o valor da hora normal). 
   
   O programa deve exibir o salário total. 
   
   Garanta que o programa trate o caso de o usuário digitar valores não 
   numéricos.
'''

# SOLICITAR OS DADOS DO USUÁRIO
horas_trabalhadas = float(input("digite o número de horas trbalhadas na semana: "))
valor_hora =  float(input("digite o valor recebido por hora: "))
# Jornada padrão de 40 horas
horas_normais = min(horas_trabalhadas, 40)
horas_extras = max(horas_trabalhadas -40, 0)
# cálculo do salário
salario_normal = horas_normais * valor_hora
salario_extra = horas_extras * valor_hora * 1.5 #50% adicional
salario_total = salario_normal + salario_extra 
# exibe o resultado
print(f"salário semanal total: R$ {salario_total: .2f}")

print("por favor, digite apenas valore numéricos.")