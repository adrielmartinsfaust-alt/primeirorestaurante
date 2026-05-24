# Sistema de Restaurante 🍕

Sistema completo de gerenciamento de restaurante em Python com interface gráfica.

## 📋 Funcionalidades

### 10 Módulos Principais:
1. **📄 Documentos** - Gerenciamento de documentos do restaurante
2. **👥 Funcionários** - Cadastro e gestão de colaboradores
3. **📦 Estoque** - Controle de ingredientes e insumos
4. **📋 Ficha Técnica** - Receitas e informações dos pratos
5. **🎉 Eventos** - Gerenciamento de eventos e reservas
6. **📅 Agenda** - Compromissos e reuniões
7. **💳 PDV** - Ponto de venda com carrinho de compras
8. **🥗 Tabela Nutricional** - Informações nutricionais dos pratos
9. **💰 Financeiro** - Controle financeiro e relatórios
10. **⚙️ Configurações** - Ajustes e preferências do sistema

## 🔐 Login

- **Usuário:** admin
- **Senha:** admin123

## 🚀 Como Executar

### Requisitos:
- Python 3.8+
- pip

### Instalação:

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar o programa
python main.py
```

## 📁 Estrutura do Projeto

```
primeirorestaurante/
├── main.py                    # Ponto de entrada
├── login.py                   # Tela de login
├── interface_principal.py     # Interface com 10 abas
├── abas/                      # Módulos das abas
│   ├── documentos.py
│   ├── funcionarios.py
│   ├── estoque.py
│   ├── ficha_tecnica.py
│   ├── eventos.py
│   ├── agenda.py
│   ├── pdv.py
│   ├── tabela_nutricional.py
│   ├── financeiro.py
│   └── configuracoes.py
├── requirements.txt           # Dependências
├── README.md                  # Este arquivo
└── .gitignore                 # Arquivos ignorados
```

## 🛠️ Dependências

- **PySimpleGUI** - Interface gráfica
- **Pillow** - Processamento de imagens
- **openpyxl** - Trabalhar com Excel

## 📝 Próximos Passos

- [ ] Implementar banco de dados (SQLite/PostgreSQL)
- [ ] Adicionar funcionalidades completas em cada aba
- [ ] Criar relatórios em PDF
- [ ] Adicionar autenticação com hash de senhas
- [ ] Implementar backup automático
- [ ] Criar API REST
- [ ] Melhorar interface gráfica

## 👤 Autor

Adriel Martins Faust

## 📄 Licença

MIT License
