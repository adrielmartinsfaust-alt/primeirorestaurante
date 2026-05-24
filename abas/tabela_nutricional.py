import PySimpleGUI as sg

def criar_layout():
    """Layout da aba Tabela Nutricional"""
    
    layout = [
        [sg.Text('TABELA NUTRICIONAL', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Prato:'), sg.InputText(key='prato_nutri', size=(30, 1))],
        [sg.Text('Calorias:'), sg.InputText(key='calorias', size=(30, 1))],
        [sg.Text('Proteína (g):'), sg.InputText(key='proteina', size=(30, 1))],
        [sg.Text('Carboidratos (g):'), sg.InputText(key='carbos', size=(30, 1))],
        [sg.Text('Gordura (g):'), sg.InputText(key='gordura', size=(30, 1))],
        [sg.Button('Adicionar Info', size=(20, 1)), sg.Button('Ver Tabela', size=(20, 1))],
        [sg.Button('Editar', size=(15, 1)), sg.Button('Remover', size=(15, 1))],
        [sg.Text('', size=(50, 1))],
        [sg.Multiline(size=(60, 10), key='log_nutri')]
    ]
    
    return layout
