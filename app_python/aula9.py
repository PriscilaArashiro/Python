import shutil
def escrever_arquivo(texto,arq,diretorio):

    arquivo = open(diretorio + arq,'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto,arq,diretorio):
    arquivo = open(diretorio + arq, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(arq,diretorio):
    arquivo = open(diretorio + arq,'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()

    aluno_notas = aluno_nota.split('\n')
    #print(aluno_notas)
    lista_media = []
    for x in aluno_notas:
        lista_notas = x.split(',')
        #print(lista_notas)
        aluno = lista_notas[0]
        #lista_aluno_notas = lista_notas
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum(int(i) for i in notas)/4
        #print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo,'D:/Projetos/Python/arquivos/Media/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,'D:/Projetos/Python/arquivos/Media/')

if __name__== '__main__':
    # aluno = 'Rafael, 10,10,5,5\n'
    # aluno2 = 'Felipe, 7,8,5,6\n'
    # aluno3 = 'Galleani, 7,8,5,6\n'
    # aluno4 = 'Cesar, 7,8,5,6\n'
    arq = 'notas.txt'
    path = 'D:/Projetos/Python/arquivos/'
    # escrever_arquivo(aluno, arq, path)
    # atualizar_arquivo(aluno2, arq, path)
    # atualizar_arquivo(aluno3,arq, path)
    # atualizar_arquivo(aluno4, arq, path)
    # ler_arquivo(arq, path)

    arq_notas = path + arq
    lista_media = media_notas(arq_notas)
    print(lista_media)
    #copia_arquivo(arq_notas)
    move_arquivo(arq_notas)
    # arquivo = open('teste.txt','w')
    # arquivo.write('Minha primeira escrita.')
    #
    # arquivo.write('\nLinha 1')
    # arquivo.close()

    #
    # arquivo = open('teste.txt','a')
    # arquivo.write('\nSegundo dia.')
    #
    # arquivo.write('\nLinha 2')
    # arquivo.close()
