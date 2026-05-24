import PySimpleGUI as sg

def criar_layout():
    """Layout da aba Funcionários"""
    
    layout = [
        [sg.Text('GERENCIAMENTO DE FUNCIONÁRIOS', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Nome:'), sg.InputText(key='nome_func', size=(30, 1))],
        [sg.Text('Cargo:'), sg.InputText(key='cargo_func', size=(30, 1))],
        [sg.Text('Telefone:'), sg.InputText(key='tel_func', size=(30, 1))],
        [sg.Button('Adicionar Funcionário', size=(20, 1)), sg.Button('Listar Funcionários', size=(20, 1))],
        [sg.Button('Editar', size=(15, 1)), sg.Button('Deletar', size=(15, 1))],
        [sg.Text('', size=(50, 2))],
        [sg.Multiline(size=(60, 15), key='log_funcionarios')]
    ]
    
    return layout
