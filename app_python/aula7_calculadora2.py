class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self,valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self,valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self,valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
#print(calculadora.valor_a)
print(calculadora.soma(10,2))
print(calculadora.subtracao(10,2))
print(calculadora.multiplicacao(10,2))
print(calculadora.divisao(10,2))
# print(soma(0,2))
# print(soma(2,4))
# print(multiplicao(10,2))
# print(divisao(10,2))

