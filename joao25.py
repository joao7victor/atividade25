# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
numero = []
for i in range ( 0, 6):
    inserirnumero = int (input (" inserir numero "))
    if inserirnumero % 2 == 0:
        numero.append(inserirNumero)
    soma = sum(numero) 
    print(soma)