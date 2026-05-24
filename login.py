import PySimpleGUI as sg

def tela_login():
    """Tela de login do sistema"""
    
    sg.theme('DarkBlue3')
    
    layout = [
        [sg.Text('', size=(30, 1))],  # Espaço
        [sg.Text('SISTEMA DE RESTAURANTE', font=('Arial', 20, 'bold'), justification='center')],
        [sg.Text('', size=(30, 1))],  # Espaço
        [sg.Text('Usuário:', font=('Arial', 12)), sg.InputText(key='usuario', size=(20, 1))],
        [sg.Text('Senha:', font=('Arial', 12)), sg.InputText(key='senha', password_char='*', size=(20, 1))],
        [sg.Text('', size=(30, 1))],  # Espaço
        [sg.Button('Login', size=(10, 1)), sg.Button('Sair', size=(10, 1))],
        [sg.Text('Usuário: admin | Senha: admin123', font=('Arial', 9), text_color='gray')]
    ]
    
    janela = sg.Window('Login', layout, finalize=True, element_justification='center')
    
    while True:
        evento, valores = janela.read()
        
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janela.close()
            return None
        
        if evento == 'Login':
            usuario = valores['usuario']
            senha = valores['senha']
            
            # Validação simples (pode ser conectado a banco de dados depois)
            if usuario == 'admin' and senha == 'admin123':
                janela.close()
                return usuario
            else:
                sg.popup_error('Usuário ou senha incorretos!', title='Erro de Login')

    return None
