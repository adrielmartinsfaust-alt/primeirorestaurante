import PySimpleGUI as sg

def criar_layout():
    """Layout da aba Eventos"""
    
    layout = [
        [sg.Text('GERENCIAMENTO DE EVENTOS', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Nome do Evento:'), sg.InputText(key='evento_nome', size=(30, 1))],
        [sg.Text('Data:'), sg.InputText(key='evento_data', size=(30, 1))],
        [sg.Text('Número de Pessoas:'), sg.InputText(key='evento_pessoas', size=(30, 1))],
        [sg.Text('Local:'), sg.InputText(key='evento_local', size=(30, 1))],
        [sg.Button('Criar Evento', size=(20, 1)), sg.Button('Listar Eventos', size=(20, 1))],
        [sg.Button('Editar', size=(15, 1)), sg.Button('Cancelar', size=(15, 1))],
        [sg.Text('', size=(50, 2))],
        [sg.Multiline(size=(60, 12), key='log_eventos')]
    ]
    
    return layout
