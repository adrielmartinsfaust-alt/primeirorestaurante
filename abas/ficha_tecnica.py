import PySimpleGUI as sg

def criar_layout():
    """Layout da aba Ficha Técnica"""
    
    layout = [
        [sg.Text('FICHA TÉCNICA DOS PRATOS', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Nome do Prato:'), sg.InputText(key='prato_nome', size=(30, 1))],
        [sg.Text('Ingredientes:'), sg.Multiline(size=(35, 5), key='prato_ingredientes')],
        [sg.Text('Modo de Preparo:'), sg.Multiline(size=(35, 5), key='prato_modo')],
        [sg.Button('Adicionar Prato', size=(20, 1)), sg.Button('Listar Pratos', size=(20, 1))],
        [sg.Button('Editar', size=(15, 1)), sg.Button('Deletar', size=(15, 1))],
        [sg.Text('', size=(50, 1))],
        [sg.Multiline(size=(60, 10), key='log_ficha')]
    ]
    
    return layout
