import pygame
import sys
from pet.pet import Pet
from ui.hud import HUD

class Game:
    def __init__(self):
        pygame.init()
        
        # Configurações da tela
        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tamagotchi")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Criar o pet
        self.pet = Pet("Tamagotchi")
        
        # HUD para renderizar a interface
        self.hud = HUD(self.WIDTH, self.HEIGHT)
        
        # Controle de tempo
        self.time_counter = 0
        self.pass_time_interval = 60  # a cada 60 frames passa 1 unidade de tempo

    def handle_events(self):
        """Trata eventos do pygame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_input(event.key)

    def handle_input(self, key):
        """Trata input do usuário"""
        if key == pygame.K_f:  # F para alimentar
            self.pet.feed()
        elif key == pygame.K_p:  # P para brincar
            self.pet.play()
        elif key == pygame.K_s:  # S para dormir
            self.pet.sleep()
        elif key == pygame.K_ESCAPE:  # ESC para sair
            self.running = False

    def update(self):
        """Atualiza a lógica do jogo"""
        self.time_counter += 1
        
        # Passa tempo a cada intervalo
        if self.time_counter >= self.pass_time_interval:
            self.pet.pass_time()
            self.time_counter = 0
        
        # Verifica se o pet morreu
        if not self.pet.is_alive():
            self.show_game_over()

    def draw(self):
        """Renderiza a tela"""
        self.screen.fill((240, 240, 240))  # Fundo branco
        
        # Renderizar HUD
        self.hud.draw(self.screen, self.pet)
        
        pygame.display.flip()

    def show_game_over(self):
        """Mostra tela de game over"""
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 - 50))
        
        subtitle_font = pygame.font.Font(None, 36)
        subtitle = subtitle_font.render(f"Seu {self.pet.name} morreu...", True, (0, 0, 0))
        subtitle_rect = subtitle.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))
        
        self.screen.fill((240, 240, 240))
        self.screen.blit(text, text_rect)
        self.screen.blit(subtitle, subtitle_rect)
        pygame.display.flip()
        
        # Espera 3 segundos e encerra
        pygame.time.wait(3000)
        self.running = False

    def run(self):
        """Loop principal do jogo"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)
        
        pygame.quit()
        sys.exit()