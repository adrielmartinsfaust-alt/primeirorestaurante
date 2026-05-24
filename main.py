import PySimpleGUI as sg
from login import tela_login
from interface_principal import interface_principal

# Configurar tema
sg.theme('DarkBlue3')
sg.set_options(font=('Arial', 10))

def main():
    # Tela de login
    usuario_logado = tela_login()
    
    if usuario_logado:
        # Se login bem-sucedido, abre interface principal
        interface_principal(usuario_logado)

if __name__ == '__main__':
    main()
