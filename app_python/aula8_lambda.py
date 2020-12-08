# def contador_letras(lista_palavras):
#     contador = []
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#
#     return contador

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro','gato','galinha']
print(contador_letras(lista_animais))

soma = lambda a,b: a + b
subtracao = lambda a,b: a - b

print(soma(5,2))
print(subtracao(6,2))

calculadora = {
    'soma': lambda a,b: a + b,
    'subtracao': lambda a,b: a - b,
    'multiplicacao': lambda a,b: a * b,
    'divisao': lambda a,b: a / b,

}

print (type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']

print('A soma é {}.' .format(soma(10,5)))
print('A multiplicacao é {}.' .format(multiplicacao(10,2)))
