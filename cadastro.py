from socket import if_nameindex
from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário:'), sg.Input(key='user', size=(20,1))],
    [sg.Text('Senha:'), sg.Input(key='password', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar dados de entrada:')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de Login', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['user'] == 'Gus' and valores['password'] == '123456':
            print('Bem vindo ao seu restaurante!')
        else:
            print('Login incorreto.')