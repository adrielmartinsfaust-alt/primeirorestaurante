import PySimpleGUI as sg

def criar_layout():
    """Layout da aba Documentos"""
    
    layout = [
        [sg.Text('GERENCIAMENTO DE DOCUMENTOS', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Button('Adicionar Documento', size=(20, 1)), sg.Button('Listar Documentos', size=(20, 1))],
        [sg.Button('Editar Documento', size=(20, 1)), sg.Button('Deletar Documento', size=(20, 1))],
        [sg.Text('', size=(50, 3))],
        [sg.Multiline(size=(60, 20), key='log_documentos')]
    ]
    
    return layout
