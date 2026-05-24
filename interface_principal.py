import PySimpleGUI as sg
from abas import documentos, funcionarios, estoque, ficha_tecnica
from abas import eventos, agenda, pdv, tabela_nutricional, financeiro, configuracoes

def interface_principal(usuario):
    """Interface principal com 10 abas"""
    
    sg.theme('DarkBlue3')
    
    # Layout das abas
    tab_grupo = [
        [sg.Tab('📄 Documentos', documentos.criar_layout())],
        [sg.Tab('👥 Funcionários', funcionarios.criar_layout())],
        [sg.Tab('📦 Estoque', estoque.criar_layout())],
        [sg.Tab('📋 Ficha Técnica', ficha_tecnica.criar_layout())],
        [sg.Tab('🎉 Eventos', eventos.criar_layout())],
        [sg.Tab('📅 Agenda', agenda.criar_layout())],
        [sg.Tab('💳 PDV', pdv.criar_layout())],
        [sg.Tab('🥗 Tabela Nutricional', tabela_nutricional.criar_layout())],
        [sg.Tab('💰 Financeiro', financeiro.criar_layout())],
        [sg.Tab('⚙️ Configurações', configuracoes.criar_layout())]
    ]
    
    layout = [
        [sg.Text(f'Bem-vindo, {usuario}! | Sistema de Restaurante', font=('Arial', 14, 'bold'))],
        [sg.TabGroup(tab_grupo, enable_events=True)],
        [sg.Button('Sair', size=(15, 1))]
    ]
    
    janela = sg.Window('Sistema de Restaurante', layout, finalize=True, size=(900, 600))
    
    while True:
        evento, valores = janela.read()
        
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            break
    
    janela.close()
