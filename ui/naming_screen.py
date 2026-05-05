import pygame
import sys
from db.database import pet_existe, carregar_pet, criar_novo_pet

class NamingScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.SysFont("Arial", 36, bold=True)
        self.font_input = pygame.font.SysFont("Arial", 24)
        self.font_button = pygame.font.SysFont("Arial", 20, bold=True)
        
        # Cores
        self.COLOR_BG = (15, 23, 42)
        self.COLOR_PANEL = (30, 41, 59)
        self.COLOR_BLUE = (59, 130, 246)
        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_GRAY = (156, 163, 175)
        
        # Estado da tela
        self.input_text = ""
        self.active = True
        self.button_hovered = False
        
        # Botão
        self.button_rect = pygame.Rect(300, 400, 200, 50)

    def draw(self):
        self.screen.fill(self.COLOR_BG)
        
        # Título
        title = self.font_title.render("Nomeie seu Tamagotchi", True, self.COLOR_WHITE)
        title_rect = title.get_rect(center=(400, 200))
        self.screen.blit(title, title_rect)
        
        # Campo de entrada
        input_bg = pygame.Rect(250, 280, 300, 50)
        pygame.draw.rect(self.screen, self.COLOR_PANEL, input_bg, border_radius=10)
        pygame.draw.rect(self.screen, self.COLOR_BLUE, input_bg, 2, border_radius=10)
        
        # Texto do input
        input_surface = self.font_input.render(self.input_text, True, self.COLOR_WHITE)
        input_rect = input_surface.get_rect(center=input_bg.center)
        self.screen.blit(input_surface, input_rect)
        
        # Placeholder se vazio
        if not self.input_text:
            placeholder = self.font_input.render("Digite o nome...", True, self.COLOR_GRAY)
            placeholder_rect = placeholder.get_rect(center=input_bg.center)
            self.screen.blit(placeholder, placeholder_rect)
        
        # Botão
        button_color = (59, 130, 246) if self.button_hovered else (30, 58, 138)
        pygame.draw.rect(self.screen, button_color, self.button_rect, border_radius=10)
        pygame.draw.rect(self.screen, self.COLOR_WHITE, self.button_rect, 2, border_radius=10)
        
        button_text = self.font_button.render("CRIAR PET", True, self.COLOR_WHITE)
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text, button_text_rect)
        
        pygame.display.flip()

    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        self.button_hovered = self.button_rect.collidepoint(mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.input_text.strip():
                    # Criar pet e sair da tela
                    if criar_novo_pet(self.input_text.strip()):
                        self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    # Adicionar caractere (limitar tamanho)
                    if len(self.input_text) < 20 and event.unicode.isprintable():
                        self.input_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_hovered and self.input_text.strip():
                    if criar_novo_pet(self.input_text.strip()):
                        self.active = False

    def run(self):
        clock = pygame.time.Clock()
        while self.active:
            self.handle_events()
            self.draw()
            clock.tick(60)
        
        # Retorna o nome do pet criado
        return self.input_text.strip()