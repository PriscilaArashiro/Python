from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras,teste
televisao = Televisao()


televisao.ligada
print(televisao.ligada)
televisao.power()
televisao.ligada
print(televisao.ligada)
televisao.aumenta_canal()
print(televisao.canal)


calculadora = Calculadora(10,2)
print(calculadora.soma())


lista = ['manga','goiaba','mamao']
total_letras = contador_letras(lista)
print('Total de letras de cada palavra da lista respecitivamente: {}' .format(total_letras))

print(teste())
