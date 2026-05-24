import PySimpleGUI as sg

def criar_layout():
    """Layout da aba PDV (Ponto de Venda)"""
    
    layout = [
        [sg.Text('PONTO DE VENDA', font=('Arial', 14, 'bold'))],
        [sg.Text('', size=(50, 1))],
        [sg.Text('Prato:'), sg.InputText(key='prato_pdv', size=(30, 1))],
        [sg.Text('Quantidade:'), sg.InputText(key='qtd_pdv', size=(30, 1))],
        [sg.Text('Preço Unitário:'), sg.InputText(key='preco_pdv', size=(30, 1))],
        [sg.Button('Adicionar ao Carrinho', size=(20, 1)), sg.Button('Ver Carrinho', size=(20, 1))],
        [sg.Button('Finalizar Venda', size=(20, 1)), sg.Button('Limpar Carrinho', size=(20, 1))],
        [sg.Text('', size=(50, 1))],
        [sg.Multiline(size=(60, 12), key='log_pdv')]
    ]
    
    return layout
