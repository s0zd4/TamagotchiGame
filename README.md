# Tamagotchi em Python com Pygame

Um jogo de tamagotchi clássico desenvolvido em Python usando a biblioteca Pygame.

## Como Jogar (Executável)

### Opção 1: Executável Direto (Recomendado)
1. **Clique duas vezes** no arquivo `Executar_Tamagotchi.bat`
2. O jogo abrirá automaticamente!

### Opção 2: Executável Manual
1. Vá para a pasta `dist/`
2. Clique duas vezes no arquivo `Tamagotchi.exe`

### Opção 3: Código Fonte (Desenvolvedores)
```bash
pip install -r requirements.txt
python main.py
```

## 🎮 Controles

- **F**: Alimentar o pet
- **P**: Brincar com o pet  
- **S**: Colocar o pet para dormir
- **H**: Curar o pet
- **ESC**: Sair do jogo

## 📊 Mecânica do Jogo

### Atributos do Pet
- **Fome**: Aumenta com o tempo, diminui ao alimentar
- **Energia**: Diminui ao brincar, regenera ao dormir
- **Felicidade**: Aumenta ao brincar, diminui naturalmente
- **Saúde**: Afetada por todos os atributos; o pet morre se chegar a 0
- **Nível**: Aumenta ganhando XP ao brincar
- **Idade**: Aumenta progressivamente

### Sistema de Sono
- Quando dormindo, a energia regenera constantemente
- Outros atributos não pioram durante o sono
- Ações ficam bloqueadas enquanto o pet dorme
- Botões ficam desabilitados visualmente

### Salvamento Automático
- Todos os dados são salvos automaticamente no banco SQLite
- O jogo carrega automaticamente o pet salvo na próxima execução
- Se for a primeira vez, você nomeia seu pet

## 📁 Estrutura do Projeto

```
tamagotchiProject/
│
├── main.py                    # Ponto de entrada do jogo
├── requirements.txt           # Dependências Python
├── Executar_Tamagotchi.bat    # Script para executar o jogo
├── dist/
│   └── Tamagotchi.exe         # Executável standalone
├── game/
│   ├── __init__.py
│   └── game.py                # Controle principal do jogo
├── pet/
│   ├── __init__.py
│   └── pet.py                 # Lógica do pet
├── ui/
│   ├── __init__.py
│   ├── hud.py                 # Interface visual
│   └── naming_screen.py       # Tela de nomeação
├── db/
│   ├── database.py            # Operações do banco
│   └── pet_info.db            # Banco de dados SQLite
└── assets/
    ├── fonts/
    ├── images/
    └── sounds/
```

## 🔧 Desenvolvimento

### Dependências
- Python 3.13+
- Pygame 2.6+

### Instalação para Desenvolvimento
```bash
pip install -r requirements.txt
```

### Criar Novo Executável
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name Tamagotchi main.py
```

## 📝 Notas Técnicas

- **Executável Standalone**: Criado com PyInstaller, não requer instalação de Python
- **Banco de Dados**: SQLite integrado, dados salvos automaticamente
- **Interface**: Pygame com animações suaves e design moderno
- **Arquitetura**: Código modular e bem organizado

Divirta-se com seu Tamagotchi! 🎮
