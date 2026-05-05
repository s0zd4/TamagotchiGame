import pygame
import sys
from pet.pet import Pet
from ui.hud import HUD

class Game:
    def __init__(self, pet):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tamagotchi Virtual")
        self.clock = pygame.time.Clock()
        
        self.pet = pet
        self.hud = HUD(self.screen.get_width(), self.screen.get_height())
        self.running = True
        
        # Contadores de tempo para diferentes atualizações
        self.needs_counter = 0
        self.age_counter = 0

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0  # Delta time em segundos
            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self):
        mouse_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True
            
            if event.type == pygame.KEYDOWN:
                # Teclas de atalho baseadas no seu pet.html
                if event.key == pygame.K_f and not self.pet.is_sleeping: # F para Comer
                    self.pet.feed()
                if event.key == pygame.K_p and not self.pet.is_sleeping: # P para Brincar
                    self.pet.play()
                if event.key == pygame.K_s: # S para Dormir (sempre disponível)
                    self.pet.toggle_sleep()
                if event.key == pygame.K_h and not self.pet.is_sleeping: # H para Curar
                    self.pet.heal()
        
        # Verifica cliques nos botões
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pressed:
            self.check_button_clicks(mouse_pos)

    def check_button_clicks(self, mouse_pos):
        """Verifica se algum botão foi clicado e executa a ação."""
        for button in self.hud.buttons:
            if button.rect.collidepoint(mouse_pos) and not button.disabled:
                if button.action == "feed":
                    self.pet.feed()
                elif button.action == "play":
                    self.pet.play()
                elif button.action == "sleep":
                    self.pet.toggle_sleep()
                elif button.action == "heal":
                    self.pet.heal()

    def update(self, dt):
        # Atualiza contadores
        self.needs_counter += dt
        self.age_counter += dt
        
        # Chama a lógica de tempo e status do pet
        self.pet.update(self.needs_counter, self.age_counter)
        
        # Atualiza animação dos status exibidos
        self.hud.update_displayed_stats(self.pet)
        
        # Reseta contadores quando atingem o limite
        if self.needs_counter >= 5:
            self.needs_counter = 0
        if self.age_counter >= 10:
            self.age_counter = 0

    def draw(self):
        # Desenha a interface com as cores do Tailwind CSS
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        self.hud.draw_game_screen(self.screen, self.pet, mouse_pos, mouse_pressed)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()