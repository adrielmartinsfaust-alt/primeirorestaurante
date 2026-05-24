import PySimpleGUI as sg

def criar_layout():
    """Layout da aba Agenda"""
    
    layout = [
        [sg.Text('AGENDA', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Compromisso:'), sg.InputText(key='compromisso', size=(30, 1))],
        [sg.Text('Data:'), sg.InputText(key='data_agenda', size=(30, 1))],
        [sg.Text('Hora:'), sg.InputText(key='hora_agenda', size=(30, 1))],
        [sg.Text('Descrição:'), sg.Multiline(size=(35, 5), key='desc_agenda')],
        [sg.Button('Agendar', size=(20, 1)), sg.Button('Ver Agenda', size=(20, 1))],
        [sg.Button('Editar', size=(15, 1)), sg.Button('Remover', size=(15, 1))],
        [sg.Text('', size=(50, 1))],
        [sg.Multiline(size=(60, 10), key='log_agenda')]
    ]
    
    return layout
