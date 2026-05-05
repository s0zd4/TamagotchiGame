import pygame
from game.game import Game
from ui.naming_screen import NamingScreen
from db.database import pet_existe, carregar_pet, inicializar_banco
from pet.pet import Pet

if __name__ == "__main__":
    # Inicializar banco de dados
    inicializar_banco()
    
    # Verificar se já existe um pet
    if pet_existe():
        # Carregar pet existente
        dados_pet = carregar_pet()
        if dados_pet:
            name, hungry, happiness, energy, health, experience, level, age = dados_pet
            pet = Pet(name, hungry, happiness, energy, health, experience, level, age)
            print(f"Carregando pet existente: {name}")
        else:
            print("Erro ao carregar pet existente, criando novo...")
            # Mostrar tela de nomeação
            pygame.init()
            screen = pygame.display.set_mode((800, 600))
            naming_screen = NamingScreen(screen)
            pet_name = naming_screen.run()
            pet = Pet(pet_name)
    else:
        # Mostrar tela de nomeação para novo pet
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        naming_screen = NamingScreen(screen)
        pet_name = naming_screen.run()
        pet = Pet(pet_name)
    
    # Iniciar jogo
    app = Game(pet)
    app.run()