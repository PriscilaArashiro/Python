lista = [1,10]
try:
    arquivo = open('teste.txt','r')
    divisao = 10 / 0
    elemento = lista[1]
    x = 1
    arquivo.close()
except ZeroDivisionError:
    print('Não é possível executar uma divisão por zero.')
except IndexError:
    print('Verifique o índice da lista.')
except Exception as ex :
    print('Erro desconhecido. Erro: {}.'.format(ex))
else:
    print('Executa quando não ocorre nenhuma exceção.')
finally:
    print('Sempre Executa')
    arquivo.close()
    if arquivo.closed == True:
        print('arquivo fechado.')