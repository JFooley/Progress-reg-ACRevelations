import time
from datetime import datetime
from PySimpleGUI import PySimpleGUI as sg

def inicio(): ### Tela inicial do programa
    layoutInicio = [
        [sg.Image(r'Tela_inicial.png')],
        [sg.Button('Fazer registro',button_color=('White','Red')),sg.Button('Sair',button_color=('White','Red'))]
                    ]

    windowInicio = sg.Window('LabEHGames - Registro AC: Revelations (Beta 2.0) by João Gabriel', layoutInicio)

    while True:
        event, values = windowInicio.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            windowInicio.close()
            quit()
        if event == 'Fazer registro':
            windowInicio.close()
            break
    
def erro(txt): ### Faz aparecer uma tela de erro
    layoutError = [
        [sg.Text(txt)],
        [sg.Button('Ok')],
        ]
             
    windowErro = sg.Window('Erro!', layoutError)
    
    while True:
        event, values = windowErro.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            windowErro.close()
            break
        
#Base de dados
seq_1 = {'Nome':'1 - Uma espécie de regresso a casa (1511)','seq1-1':'1 - O Hangman\nViaje para Masyaf e fuja dos Templários que chegaram lá antes de você.',
         'seq1-2':'2 - Uma Fuga Estreita\nEncontre seu equipamento e continue sua busca pela biblioteca.',
         'seq1-3':'3 - Um diário de algum tipo\nDepois de encontrar a entrada da biblioteca, descubra que entrar não será tão fácil.',
         'seq1-4':'4 - Um passeio difícil\nTente recuperar o diário de Leandros.',
         'seq1-5':'5 - A Águia Ferida\nCure-se e mate Leandros.',
         'seq1-6':'6 - Ilha do Animus\nSaiba mais sobre sua estada involuntária no Animus.'}
keys_seq_1 = []
for i in seq_1:
    keys_seq_1.append(i)

seq_2 = {'Nome':'2 - A Encruzilhada do Mundo (1511)',
         'seq2-1':'1 - Boas-vindas calorosas\nChegue em Constantinopla, encontre Yusuf pela primeira vez e aprenda sobre os problemas locais.',
         'seq2-2':'2 - Atualizar e explorar\nAtualize seu equipamento.',
         'seq2-3':'3 - O Hookblade\nAprenda a usar seu novo Hookblade.',
         'seq2-4':'4 - A Vista de Galata\nUse suas novas habilidades para subir ao topo da Torre Galata.',
         'seq2-5':'5 - Táticas Avançadas\nColoque suas habilidades em um novo uso enquanto você e Yusuf se preparam para defender antros de assassinos.',
         'seq2-6':'6 - Na Defesa\nDefenda o covil de Galata de um ataque dos Templários.',
         'seq2-7':'7 - No Ataque\nSaiba mais sobre as bombas dos assassinos e recupere um covil que foi tomado pelos Templários.'}
keys_seq_2 = []
for i in seq_2:
    keys_seq_2.append(i)

seq_3 = {'Nome':'3 - Achados e Perdidos (1511)',
         'seq3-1':'1 - O Prisioneiro\nLiberte o homem que foi preso por roubar comida.',
         'seq3-2':'2 - O Sentinela, Parte 1\nConverse com seu Aprendiz e saiba mais sobre o Sentinela.',
         'seq3-3':'3 - Contratos de Guilda\nEnvie seu Aprendiz em uma missão contratada.',
         'seq3-4':'4 - Fabricação de bombas\nAprenda a fabricar explosivos',
         'seq3-5':'5 - Um rosto familiar\nEncontre a porta escondida na livraria de Sofia.',
         'seq3-6':'6 - A Cisterna de Yerebatan\nInvestigue a cisterna subterrânea e procure sua primeira Chave Masyaf.',
         'seq3-7':'7 - Quid Pro Quo\nVolte para a livraria e mostre a Sofia o que você encontrou.',
         'seq3-8':'8 - O Guardião do Mentor\nLute até a fortaleza Masyaf e salve Al Mualim.',
         'seq3-9':'9 - Maldição do Romani\nEnvenene os Templários Bizantinos e recupere o baú roubado.',
         'seq3-10':'10 - O Sentinela, Parte 2\nLide com o traidor.'}
keys_seq_3 = []
for i in seq_3:
    keys_seq_3.append(i)

seq_4 = {'Nome':'4 - A Guerra Incivil (1511)',
         'seq4-1':'1 - Banquete do Príncipe\nProteja os otomanos e ganhe sua confiança.',
         'seq4-2':'2 - Uma reunião desconfortável\nEscute a conversa de Suleiman com Tarik Barleti.',
         'seq4-3':'3 - A Quarta Parte do Mundo\nA entrega de Sofia está envolvida na burocracia. Recupere para ela ..',
         'seq4-4':'4 - Sinais e Símbolos, Parte I\nVá até a Hagia Sophia e procure o livro que Niccolò Polo deixou para trás',
         'seq4-5':'5 - Torre Galata\nEstacione seu caminho pela Torre Galata e localize outra chave Masyaf.',
         'seq4-6':'6 - O Despertar do Mentor\nQueime o corpo de Al Mualim e recupere a Maçã de Abbas.'}
keys_seq_4 = []
for i in seq_4:
    keys_seq_4.append(i)

seq_5 = {'Nome':'5 - Herdeiro do Império (1511)',
         'seq5-1':'1 - Os janízaros\nSiga o capitão dos Janízaros e tente descobrir seus segredos relacionados aos Templários.',
         'seq5-2':'2 - Os portões do Arsenal\nIncite um motim para distrair os guardas e obter acesso ao Arsenal.',
         'seq5-3':'3 - Infiltração de arsenal\nDescubra o propósito da visita de Manuel.',
         'seq5-4':'4 - Retrato de uma senhora\nRecupere a pintura de Sofia.',
         'seq5-5':'5 - Sinais e Símbolos, Parte II\nProcure os símbolos do Polo perto do Aqueduto de Valens e localize o livro escondido.',
         'seq5-6':'6 - O Fórum do Boi\nRecupere a terceira Chave Masyaf no Fórum do Boi.',
         'seq5-7':'7 - Um Novo Regime\nEnfrente Abbas, depois de saber da morte de seu filho mais novo.'}
keys_seq_5 = []
for i in seq_5:
    keys_seq_5.append(i)

seq_6 = {'Nome':'6 - Desfavor da fortuna (1511)',
         'seq6-1':'1 - Nas Sombras\nAdquira um disfarce de Janízaro para se aproximar de Tarik.',
         'seq6-2':'2 - Honra, Perdido e Ganhado\nSiga os janízaros e descubra a localização das armas de Manuel.',
         'seq6-3':'3 - Portador de Notícias Mistas\nViaje ao Palácio de Topkapi para falar com Suleiman, informando-o da inocência de Tarik.',
         'seq6-4':'4 - Um pequeno recado\nFaça uma tarefa para Sofia enquanto ela localiza o último livro de Polo.',
         'seq6-5':'5 - Sinais e Símbolos, Parte III\nProcure os símbolos do Polo perto da Pequena Hagia Sophia.',
         'seq6-6':'6 - Torre da Donzela\nRecupere a Chave Masyaf escondida embaixo da torre.',
         'seq6-7':'7 - O retorno do mentor\nReúna aliados em Masyaf e elimine Abbas.',
         'seq6-8':'8 - Partindo da vela\nFuja dos janízaros e saia da cidade, em busca de Manuel.',}
keys_seq_6 = []
for i in seq_6:
    keys_seq_6.append(i)

seq_7 = {'Nome':'7 - O Submundo',
         'seq7-1':'1 - A cidade oculta\nLocalize os espiões otomanos desaparecidos e trabalhe com eles para encontrar os Templários.',
         'seq7-2':'2 - O espião que me evitou\nEncontre e resgate Dilara antes que seja tarde demais.',
         'seq7-3':'3 - O Renegado\nMate Shakhulu antes que mais prisioneiros morram.',
         'seq7-4':'4 - Descomissionado\nInfiltre-se no depósito de armas e destrua a pólvora.',
         'seq7-5':'5 - Último dos Palaiologi\nAproveite a oportunidade para matar Manuel e recuperar a chave Masyaf final.',
         'seq7-6':'6 - Fuja em\ndireção a Constantinopla, após os Templários ameaçarem matar Sofia.',
         'seq7-7':'7 - Passando a Tocha\nEscolte os irmãos Polo com segurança para fora da vila Masyaf.'}
keys_seq_7 = []
for i in seq_7:
    keys_seq_7.append(i)

seq_8 = {'Nome':'8 - The End of an Era (1511)',
         'seq8-1':'1 - Descoberta\nO Príncipe Ahmet ameaçou fazer mal a Sofia. Encontre e proteja-a.',
         'seq8-2':'2 - A Troca\nColete as Chaves Masyaf e entregue-as a Ahmet para salvar Sofia.',
         'seq8-3':'3 - Fim da Estrada\nPegue Ahmet antes que ele escape com as Chaves Masyaf.'}
keys_seq_8 = []
for i in seq_8:
    keys_seq_8.append(i)

seq_9 = {'Nome':'9 - Revelações (1511)',
         'seq9-1':'1 - Um regresso a casa\nUse as Chaves Masyaf para abrir a biblioteca de Altaïr.',
         'seq9-2':'2 - Legado perdido\nAltair esvaziou o castelo Masyaf e despachou seus Assassinos pelo mundo. Agora ele tem apenas mais uma tarefa ....',
         'seq9-3':'3 - A Mensagem\nLocalize a Maçã do Éden de Altaïr e aprenda sobre "a revelação".'}
keys_seq_9 = []
for i in seq_9:
    keys_seq_9.append(i)

seq_list = seq_1['Nome'], seq_2['Nome'], seq_3['Nome'], seq_4['Nome'], seq_5['Nome'], seq_6['Nome'], seq_7['Nome'], seq_8['Nome'], seq_9['Nome']


# TEMA DA JANELA
sg.theme('DarkAmber')

# Janela de inicio
inicio()

#Layouts #  sg.Checkbox('',key='seq',size=(25,1))
layout_seq1 = [
    [sg.Checkbox('1 - O Hangman',key='seq1-1',size=(25,1)),sg.Checkbox('2 - Uma Fuga Estreita',key='seq1-2',size=(25,1)),sg.Checkbox('3 - Um diário de algum tipo',key='seq1-3',size=(25,1))],
    [sg.Checkbox('4 - Um passeio difícil',key='seq1-4',size=(25,1)),sg.Checkbox('5 - A Águia Ferida',key='seq1-5',size=(25,1)),sg.Checkbox('6 - Ilha do Animus',key='seq1-6',size=(25,1))]
    ]

layout_seq2 = [
    [sg.Checkbox('1 - Boas-vindas calorosas',key='seq2-1',size=(25,1)),sg.Checkbox('2 - Atualizar e explorar',key='seq2-2',size=(25,1)),sg.Checkbox('3 - O Hookblade',key='seq2-3',size=(25,1))],
    [sg.Checkbox('4 - A Vista de Galata',key='seq2-4',size=(25,1)),sg.Checkbox('5 - Táticas Avançadas',key='seq2-5',size=(25,1)),sg.Checkbox('6 - Na Defesa',key='seq2-6',size=(25,1))],
    [sg.Checkbox('7 - No Ataque',key='seq2-7',size=(25,1))]
    ]

layout_seq3 = [
    [sg.Checkbox('1 - O Prisioneiro',key='seq3-1',size=(25,1)),sg.Checkbox('2 - O Sentinela, Parte 1',key='seq3-2',size=(25,1)),sg.Checkbox('3 - Contratos de Guilda',key='seq3-3',size=(25,1))],
    [sg.Checkbox('4 - Fabricação de bombas',key='seq3-4',size=(25,1)),sg.Checkbox('5 - Um rosto familiar',key='seq3-5',size=(25,1)),sg.Checkbox('6 - A Cisterna de Yerebatan',key='seq3-6',size=(25,1))],
    [sg.Checkbox('7 - Quid Pro Quo',key='seq3-7',size=(25,1)),sg.Checkbox('8 - O Guardião do Mentor',key='seq3-8',size=(25,1)),sg.Checkbox('9 - Maldição do Romani',key='seq3-9',size=(25,1))],
    [sg.Checkbox('10 - O Sentinela, Parte 2',key='seq3-10',size=(25,1))]
    ]

layout_seq4 = [
    [sg.Checkbox('1 - Banquete do Príncipe',key='seq4-1',size=(25,1)),sg.Checkbox('2 - Uma reunião desconfortável',key='seq4-2',size=(25,1)),sg.Checkbox('3 - A Quarta Parte do Mundo',key='seq4-3',size=(25,1))],
    [sg.Checkbox('4 - Sinais e Símbolos, Parte I',key='seq4-4',size=(25,1)),sg.Checkbox('5 - Torre Galata',key='seq4-5',size=(25,1)),sg.Checkbox('6 - O Despertar do Mentor',key='seq4-6',size=(25,1))]
    ]

layout_seq5 = [
    [sg.Checkbox('1 - Os janízaros',key='seq5-1',size=(25,1)),sg.Checkbox('2 - Os portões do Arsenal',key='seq5-2',size=(25,1)),sg.Checkbox('3 - Infiltração de arsenal',key='seq5-3',size=(25,1))],
    [sg.Checkbox('4 - Retrato de uma senhora',key='seq5-4',size=(25,1)),sg.Checkbox('5 - Sinais e Símbolos, Parte II',key='seq5-5',size=(25,1)),sg.Checkbox('6 - O Fórum do Boi',key='seq5-6',size=(25,1))],
    [sg.Checkbox('7 - Um Novo Regime',key='seq5-7',size=(25,1))]
    ]

layout_seq6 = [
    [sg.Checkbox('1 - Nas Sombras',key='seq6-1',size=(25,1)),sg.Checkbox('2 - Honra, Perdido e Ganhado',key='seq6-2',size=(25,1)),sg.Checkbox('3 - Portador de Notícias Mistas',key='seq6-3',size=(25,1))],
    [sg.Checkbox('4 - Um pequeno recado',key='seq6-4',size=(25,1)),sg.Checkbox('5 - Sinais e Símbolos, Parte III',key='seq6-5',size=(25,1)),sg.Checkbox('6 - Torre da Donzela',key='seq6-6',size=(25,1))],
    [sg.Checkbox('7 - O retorno do mentor',key='seq6-7',size=(25,1)),sg.Checkbox('8 - Partindo da vela',key='seq6-8',size=(25,1))]
    ]

layout_seq7 = [
    [sg.Checkbox('1 - A cidade oculta',key='seq7-1',size=(25,1)),sg.Checkbox('2 - O espião que me evitou',key='seq7-2',size=(25,1)),sg.Checkbox('3 - O Renegado',key='seq7-3',size=(25,1))],
    [sg.Checkbox('4 - Descomissionado',key='seq7-4',size=(25,1)),sg.Checkbox('5 - Último dos Palaiologi',key='seq7-5',size=(25,1)),sg.Checkbox('6 - Fuja em',key='seq7-6',size=(25,1))],
    [sg.Checkbox('7 - Passando a Tocha',key='seq7-7',size=(25,1))]
    ]

layout_seq8 = [
    [sg.Checkbox('1 - Descoberta',key='seq8-1',size=(25,1)),sg.Checkbox('2 - A Troca',key='seq8-2',size=(25,1)),sg.Checkbox('3 - Fim da Estrada',key='seq8-3',size=(25,1))]
    ]

layout_seq9 = [
    [sg.Checkbox('1 - Um regresso a casa',key='seq9-1',size=(25,1)),sg.Checkbox('2 - Legado perdido',key='seq9-2',size=(25,1)),sg.Checkbox('3 - A Mensagem',key='seq9-3',size=(25,1))]
    ]

layout1 = [ [sg.Text(45*' '),sg.Text("Registro de atividade Assasin's Creed: Revelations\n")],
            [sg.Text(35*' '),sg.Text('Preencha os campos abaixo e confirme para gerar o registro em .TXT\n')],
            [sg.Text('Início da jogatina (HH:MM)'), sg.InputText(size=(5,1),key='hora1'), sg.Text('Fim da jogatina (HH:MM)'), sg.InputText(size=(5,1),key='hora2')],
            [sg.Text('')],
            [sg.Text('Qual sequência foi feita?')],
            [sg.InputCombo(('1 - Uma espécie de regresso a casa (1511)','2 - A Encruzilhada do Mundo (1511)','3 - Achados e Perdidos (1511)','4 - A Guerra Incivil (1511)',
                            '5 - Herdeiro do Império (1511)','6 - Desfavor da fortuna (1511)','7 - O Submundo','8 - The End of an Era (1511)', '9 - Revelações (1511)'),
                           size=(35, 1),key='Sequencia')],
            [sg.Text('Quais memórias foram feitas?')],
            [sg.TabGroup([[sg.Tab('1',layout_seq1),sg.Tab('2',layout_seq2),sg.Tab('3',layout_seq3),sg.Tab('4',layout_seq4),sg.Tab('5',layout_seq5),
                           sg.Tab('6',layout_seq6),sg.Tab('7',layout_seq7),sg.Tab('8',layout_seq8),sg.Tab('9',layout_seq9)]])],
            [sg.Text('Quais foram os avanços?\n(Progressos in game, Mecanicas, Database, Itens...)')],
            [sg.InputText(size=(100,40),key='avancos')],
            [sg.Text('Qual foi a progressão da narrativa?\n(Progressões na Narrativa historica do jogo)')],
            [sg.InputText(size=(100,40),key='narra')],
            [sg.Text('Apontamentos:\n(Referencias históricas e outras Observações)')],
            [sg.InputText(size=(100,40),key='points')],
            [sg.Text('')],
            [sg.Button('Confirmar dados')]
             ]

layout2 = [ [sg.Text('Dados confirmados!')],
            [sg.Text('Arquivo Txt gerado')],
            [sg.Button('Fechar')]
            ]



# Janela principal
window = sg.Window('LabEHGames - Registro AC: Revelations (Beta 2.0) by João Gabriel', layout1)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        window.close()
        quit()
        
    if event == 'Confirmar dados':
        
        hora1 = values['hora1']
        if hora1 == '':
            erro('Campo do início da jogatina vazio!')
            continue
        if len(hora1) != 5 or hora1[2] != ':':
            erro('Entrada inválida!')
            continue
        check_hora = hora1.split(':')
        if check_hora[0].isnumeric() == False or check_hora[1].isnumeric() == False:
            erro('Entrada inválida!')
            continue
        elif int(check_hora[0]) > 23 or int(check_hora[0]) < 0:
            erro('Hora inválida!')
            continue
        elif int(check_hora[1]) > 59 or int(check_hora[1]) < 0:
            erro('Minutos inválidos!')
            continue
        
        hora2 = values['hora2']
        if hora2 == '':
            erro('Campo do fim da jogatina vazio!')
            continue
        if len(hora2) != 5 or hora1[2] != ':':
            erro('Entrada inválida!')
            continue
        check_hora = hora2.split(':')
        if check_hora[0].isnumeric() == False or check_hora[1].isnumeric() == False:
            erro('Entrada inválida!')
            continue
        elif int(check_hora[0]) > 23 or int(check_hora[0]) < 0:
            erro('Hora inválida!')
            continue
        elif int(check_hora[1]) > 59 or int(check_hora[1]) < 0:
            erro('Minutos inválidos!')
            continue
        
        horas_jogadas = hora1 + ' - ' + hora2

        data_hora = datetime.now()
        data_hora = data_hora.strftime('%d/%m/%Y %H:%M')

        if values['Sequencia'] == '':
            erro('Sequência não selecionada!')
            continue
        sequencia = values['Sequencia']

        memorias = ''
        for n in keys_seq_1:    #1 ---------------
            if n == keys_seq_1[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_1[n] + '\n'
        for n in keys_seq_2:    #2 ---------------
            if n == keys_seq_2[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_2[n] + '\n'
        for n in keys_seq_3:    #3 ---------------
            if n == keys_seq_3[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_3[n] + '\n'
        for n in keys_seq_4:    #4 ---------------
            if n == keys_seq_4[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_4[n] + '\n'
        for n in keys_seq_5:    #5 ---------------
            if n == keys_seq_5[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_5[n] + '\n'
        for n in keys_seq_6:    #6 ---------------
            if n == keys_seq_6[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_6[n] + '\n'
        for n in keys_seq_7:    #7 ---------------
            if n == keys_seq_7[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_7[n] + '\n'
        for n in keys_seq_8:    #8 ---------------
            if n == keys_seq_8[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_8[n] + '\n'
        for n in keys_seq_9:    #9 ---------------
            if n == keys_seq_9[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_9[n] + '\n'
        
        avancos = values['avancos']
        if avancos == '':
            erro('Campo de avanços em branco!')
            continue
        
        narra = values['narra']
        if narra == '':
            erro('Campo de narrativa em branco!')
            continue
        
        points = values['points']
        if points == '':
            erro('Campo de apontamentos em branco!')
            continue
        
        break

window.close()

# Janela secundária
window2 = sg.Window('LabEHGames - Confirmado!', layout2)

final = 'Assassins Creed: Revelations\n\n' + 'Data: ' + data_hora + '\n' + 'Horas jogadas: ' + horas_jogadas + '\n\n' + 'Sequencia ' + sequencia + '\n\n' + 'Memorias feitas:\n' + memorias + '\n' + 'Avanços:\n' + avancos + '\n\n' + 'Narrativa:\n' + narra + '\n\n' + 'Apontamentos:\n' + points + '\n\n '
with open('Realatório.txt','w') as regdados:
    regdados.write(str(final))

while True:
    event, values = window2.read()
    if event == sg.WIN_CLOSED or event == 'Fechar': # if user closes window or clicks cancel
        window2.close()
        quit()
