import PySimpleGUI as sg

def criar_layout():
    """Layout da aba Financeiro"""
    
    layout = [
        [sg.Text('CONTROLE FINANCEIRO', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Descrição:'), sg.InputText(key='desc_fin', size=(30, 1))],
        [sg.Text('Valor:'), sg.InputText(key='valor_fin', size=(30, 1))],
        [sg.Text('Tipo:'), sg.Combo(['Receita', 'Despesa'], key='tipo_fin', size=(28, 1))],
        [sg.Text('Data:'), sg.InputText(key='data_fin', size=(30, 1))],
        [sg.Button('Registrar', size=(20, 1)), sg.Button('Ver Relatório', size=(20, 1))],
        [sg.Button('Editar', size=(15, 1)), sg.Button('Deletar', size=(15, 1))],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Saldo Total: R$ 0.00', font=('Arial', 12, 'bold'), text_color='green')],
        [sg.Multiline(size=(60, 10), key='log_financeiro')]
    ]
    
    return layout
