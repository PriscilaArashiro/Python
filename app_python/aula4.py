# a = int(input('Digite um número inteiro: '))
# div = 0
# resto = 0
# for x in range(1,a + 1):
#     resto = a % x
#   #  print(a,x,resto)
#     if resto == 0:
#         div +=1
# if div == 2 :
#     print('O número {} é primo.' .format(a))
# else:
#     print('O número {} não é primo.'.format(a))
# a = int(input('Digite um número inteiro: '))
# for num in range(a + 1):
#
#     div = 0
#     resto = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         #print(num, x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print('O número {} é primo.'.format(num))

#
#
# a = 0
# while a <= 10:
#     print(a)
#     a += 1
#
# for x in range(100):
#     print(x)


nota =int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Nota inválida. Entre com a nota: '))
print(nota)