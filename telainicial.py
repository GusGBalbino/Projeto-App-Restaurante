from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')

layout1 = [
    [sg.Text('BEM-VINDO AO SEU RESTAURANTE')],
    [sg.Button('Entrar'), sg.Button('Cadastrar-se')] 
]

layout2 = [
    [sg.Text('Usuário:'), sg.Input(key='user', size=(30,2))],
    [sg.Text('Senha:'), sg.Input(key='password', password_char='*', size=(30,2))],
    [sg.Button('Entrar'), sg.Button('Voltar')]

]

layout3 = [
    [sg.Text('Crie um nome de usuário:'), sg.Input(key='new_user', size=(30,2))],
    [sg.Text('Crie uma senha:'), sg.Input(key='new_password', size=(30,2))],
    [sg.Button('Voltar')]
]

#Janelas
janela1 = sg.Window('Tela Inicial', layout1)
janela2 = sg.Window('Tela de Login', layout2)
janela3 = sg.Window('Tela de Cadastro', layout3)

#Ler os eventos de Login
while True:
    eventos, valores = janela1.read()

    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Voltar':
       ...

    if eventos == 'Entrar':
        eventos, valores = janela2.read()
        if valores['user'] == 'Gus' and valores['password'] == '123456':
            print('Bem vindo ao seu restaurante!')
        else:
            print('Login incorreto!')

    if eventos == 'Cadastrar-se':
        eventos, valores = janela3.read()
