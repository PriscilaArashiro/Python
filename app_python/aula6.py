conjunto = {1,2,3,4,4,2}
print(conjunto)
conjunto.add(5)
conjunto.discard(2)
# conjunto.remove(2)
print(conjunto)

# conjunto_material = {'telha','tijolo'}
# print(conjunto_material)
#
conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

conjunto_uniao2 = conjunto2.union(conjunto)
print('União2: {}'.format(conjunto_uniao2))

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))


conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))


conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simétrica: {}' .format(conjunto_diff_simetrica))

conjunto2_diff_simetrica = conjunto2.symmetric_difference(conjunto)
print('Diferença Simétrica2: {}' .format(conjunto2_diff_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_subset1 = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B: {}' .format(conjunto_subset1))


conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print('B é um subconjunto de A: {}' .format(conjunto_subset2))

conjunto_superset1 = conjunto_b.issuperset(conjunto_a)
print('A é um suuperconjunto de B: {}' .format(conjunto_superset1))

conjunto_superset2 = conjunto_a.issuperset(conjunto_b)
print('B é um suuperconjunto de A: {}' .format(conjunto_superset2))

lista = ['cachorro','cachorro','gato', 'gato','elefante']
conjunto_animais = set(lista)
print(conjunto_animais)

lista_animais = list(conjunto_animais)
print(lista_animais)