#01 - Desenvolva um programa em Python que solicite ao usuário o valor do raio de um círculo e, em seguida,
# calcule e exiba a área do círculo. Utilize a fórmula da área do círculo. Considere o valor de π = 3.1416

#convert a string para um float2


raio = float(input('Informe o raio: '))

area = 3.1416 * (raio ** 2)

print(f'A área do círculo de raio = {raio} é {area}')
