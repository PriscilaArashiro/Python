from datetime import date, time, datetime,timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    #print(data_atual.strftime('%d/%m/%Y %H:%M:$S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sabado','Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2020,9,19,1,35,10)
    print(data_criada.strftime('%c'))

    data_string = '19/09/1975 01:35:10'
    data_convertida = datetime.strptime(data_string,'%d/%m/%Y %H:%M:%S')

    print(data_convertida)
    print(tupla[data_convertida.weekday()])

    idade =  data_criada- data_convertida
    print(idade.days)
    idade_convertida = int(idade.days)
    print(int(idade_convertida/365))


    nova_data = data_criada  - timedelta(days=365,hours=1,minutes=20)
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A %B %Y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18,second=30)
    horario_str =horario.strftime('%H:%M:%S')
    print(type(horario_str))
if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()