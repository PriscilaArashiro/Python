a = int(input('Primeiro Bimestre: '))
while a>10:
    a = int(input('A nota deve ser menor ou igual a 10. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
while b>10:
    b = int(input('A nota deve ser menor ou igual a 10. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
while c>10:
    c = int(input('A nota deve ser menor ou igual a 10. Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
while d>10:
    d = int(input('A nota deve ser menor ou igual a 10. Quarto Bimestre: '))

media = (a + b + c + d)/4
print('Média: {}' .format(media) )


# a = int(input('Primeiro Valor: '))
# b = int(input('Segundo Valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Um número par foi digitado.')
# else:
#     print('Nenhum número par foi digitado.')

# if resto == 0:
#     print('O número é par.')
# else:
#     print('O número é impar.')

# a = int(input('Primeiro Valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro Valor: '))
#
#
# if a>b and a>c:
#     print('O maior valor é {}' .format(a))
# elif b>a and b>c:
#     print('O maior valor é {}' .format(b))
# else:
#     print('O maior valor é {}' .format(c))
#
# print('Final do Programa')