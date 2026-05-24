import PySimpleGUI as sg

def criar_layout():
    """Layout da aba Configurações"""
    
    layout = [
        [sg.Text('CONFIGURAÇÕES DO SISTEMA', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Checkbox('Modo Escuro', key='modo_escuro', default=True)],
        [sg.Checkbox('Notificações Ativas', key='notificacoes', default=True)],
        [sg.Checkbox('Backup Automático', key='backup', default=True)],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Número da Loja:'), sg.InputText(key='loja_numero', size=(30, 1))],
        [sg.Text('Nome da Loja:'), sg.InputText(key='loja_nome', size=(30, 1))],
        [sg.Text('Telefone:'), sg.InputText(key='loja_tel', size=(30, 1))],
        [sg.Text('Endereço:'), sg.InputText(key='loja_endereco', size=(30, 1))],
        [sg.Text('', size=(50, 1))],
        [sg.Button('Salvar Configurações', size=(20, 1)), sg.Button('Restaurar Padrão', size=(20, 1))],
        [sg.Button('Fazer Backup', size=(20, 1)), sg.Button('Sobre o Sistema', size=(20, 1))],
        [sg.Text('', size=(50, 1))],
        [sg.Multiline(size=(60, 8), key='log_config')]
    ]
    
    return layout
