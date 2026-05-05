from game.game import Game
import os

if __name__ == "__main__":
    # Garante a criação da pasta da base de dados se não existir
    if not os.path.exists('db'):
        os.makedirs('db')
    
    # Inicia a aplicação
    app = Game()
    app.run()