# a = 10
# b = 5
a = int(input('Entre com o valor de a:'))
b = int(input('Entre com o valor de b:'))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
# print(type(soma))
# print('Soma: ' + str(soma))
# print(subtracao)
# print(multiplicacao)
# print(int(divisao))
# print(resto)

#print ('Soma: {} .Subtração: {}'.format(soma, subtracao))
print('Soma: {soma}, Subtração: {subtracao}'.format(soma=soma, subtracao= subtracao))
# print('Soma: {soma} '
#       '\nSubtração: {sub} '
#       '\nMultiplicação: {multi} '
#       '\nDivisão: {div} '
#       '\nResto: {resto}'.format(
#          soma=soma,
#          sub= subtracao,
#          multi=multiplicacao,
#          div=divisao,
#          resto=resto))


resultado = ('Soma: {soma} '
      '\nSubtração: {sub} '
      '\nMultiplicação: {multi} '
      '\nDivisão: {div} '
      '\nResto: {resto}'.format(
            soma=soma,
            sub= subtracao,
            multi=multiplicacao,
            div=divisao,
            resto=int(resto)))

print(resultado)