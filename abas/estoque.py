import PySimpleGUI as sg

def criar_layout():
    """Layout da aba Estoque"""
    
    layout = [
        [sg.Text('CONTROLE DE ESTOQUE', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Ingrediente:'), sg.InputText(key='ingrediente', size=(30, 1))],
        [sg.Text('Quantidade:'), sg.InputText(key='quantidade', size=(30, 1))],
        [sg.Text('Unidade:'), sg.Combo(['kg', 'L', 'unidade', 'g'], key='unidade', size=(28, 1))],
        [sg.Button('Adicionar Item', size=(20, 1)), sg.Button('Listar Estoque', size=(20, 1))],
        [sg.Button('Editar', size=(15, 1)), sg.Button('Remover', size=(15, 1))],
        [sg.Text('', size=(50, 2))],
        [sg.Multiline(size=(60, 15), key='log_estoque')]
    ]
    
    return layout
