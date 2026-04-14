# Tamagotchi em Python com Pygame

Um jogo de tamagotchi clássico desenvolvido em Python usando a biblioteca Pygame.

## 📁 Estrutura do Projeto

```
tamagotchiProject/
│
├── main.py              # Ponto de entrada do jogo
├── game/
│   ├── __init__.py
│   └── game.py          # Controle principal do jogo, loop e eventos
├── pet/
│   ├── __init__.py
│   └── pet.py           # Lógica do pet (atributos, ações, comportamentos)
├── ui/
│   ├── __init__.py
│   └── hud.py           # Interface visual (HUD) e renderização
└── assets/
    ├── fonts/
    ├── images/
    └── sounds/
```

## 📋 Descrição dos Arquivos

### `main.py`
Arquivo principal que inicia o jogo. Importa a classe `Game` e executa o loop principal.

### `game/game.py`
Gerencia todo o controle do jogo:
- **Inicialização**: pygame, tela, FPS, configurações
- **Loop Principal**: atualiza lógica, renderiza e trata eventos
- **Eventos**: captura input do usuário (teclado, mouse)
- **Game Over**: verifica se o pet morreu e exibe tela de fim de jogo

### `pet/pet.py`
Define a lógica completa do pet (animal de estimação):
- **Atributos**: fome, energia, felicidade, saúde, nível, XP, idade
- **Ações**: alimentar, brincar, dormir
- **Dinâmica**: o tempo passa e afeta os atributos
- **Progressão**: sistema de níveis baseado em XP
- **Morte**: o pet morre se a saúde chegar a 0

### `ui/hud.py`
Responsável pela renderização da interface visual:
- **Titel e Status**: nome e nível do pet
- **Barras de Status**: fome, energia, felicidade e saúde
- **Informações**: XP e idade do pet
- **Controles**: exibe as teclas disponíveis na tela

## 🎮 Como Jogar

1. **Instale o pygame**:
   ```bash
   pip install pygame
   ```

2. **Execute o jogo**:
   ```bash
   python main.py
   ```

3. **Controles**:
   - **F**: Alimentar o pet
   - **P**: Brincar com o pet
   - **S**: Colocar o pet para dormir
   - **ESC**: Sair do jogo

## 📊 Mecânica do Jogo

### Atributos do Pet
- **Fome**: Aumenta com o tempo, diminui ao alimentar
- **Energia**: Diminui ao brincar, recupera ao dormir
- **Felicidade**: Aumenta ao brincar, diminui naturalmente
- **Saúde**: Afetada por todos os atributos; o pet morre se chegar a 0
- **Nível**: Aumenta ganhando XP ao brincar
- **Idade**: Aumenta progressivamente

### Dinâmica
O tempo passa automaticamente a cada 1 segundo (60 frames), afetando os atributos do pet.

Para manter o pet vivo:
- Alimente-o quando estiver com fome
- Deixe-o brincar para ganhar felicidade e XP
- Deixe-o dormir para recuperar energia

## 🔧 Possíveis Melhorias Futuras

- [ ] Adicionar sprites e animações do pet
- [ ] Adicionar efeitos sonoros
- [ ] Implementar salvamento/carregamento de jogo
- [ ] Adicionar diferentes tipos de pets
- [ ] Sistema de comidas diferentes
- [ ] Minigames para brincar
- [ ] Tela de menu principal
- [ ] Sistema de pontuação/ranking

## 📝 Notas

- O projeto está organizado de forma modular, facilitando futuras expansões
- Cada módulo tem uma responsabilidade específica
- O código está comentado para facilitar manutenção

Divirta-se! 🎮
