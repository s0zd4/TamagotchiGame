import pygame

class Button:
    def __init__(self, x, y, w, h, text, color, hover_color, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.is_hovered = False

    def draw(self, screen, font):
        # Efeito de sombra para profundidade
        shadow_rect = self.rect.copy()
        shadow_rect.y += 4
        pygame.draw.rect(screen, (15, 23, 42), shadow_rect, border_radius=12)
        
        # Desenha o botão principal
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect, border_radius=12)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2, border_radius=12)
        
        # Texto do botão
        txt_surf = font.render(self.text, True, (255, 255, 255))
        screen.blit(txt_surf, txt_surf.get_rect(center=self.rect.center))

class HUD:
    def __init__(self, w, h):
        self.w, self.h = w, h
        # Paleta de Cores "Modern Navy"
        self.COLOR_BG = (26, 26, 46)
        self.COLOR_PANEL = (31, 41, 55)
        self.COLOR_BLUE = (59, 130, 246)
        self.COLOR_RED = (220, 38, 38)
        self.COLOR_YELLOW = (202, 138, 4)
        self.COLOR_GREEN = (22, 163, 74)
        
        self.font_b = pygame.font.SysFont("Arial", 22, bold=True)
        self.font_s = pygame.font.SysFont("Arial", 14, bold=True)
        self.font_xs = pygame.font.SysFont("Arial", 12)

        # Configuração dos Botões de Ação
        bw, bh = 170, 50
        self.buttons = [
            Button(30, h - 130, bw, bh, "ALIMENTAR (F)", (185, 28, 28), (220, 38, 38), "feed"),
            Button(w - 200, h - 130, bw, bh, "BRINCAR (P)", (29, 78, 216), (59, 130, 246), "play"),
            Button(30, h - 70, bw, bh, "DORMIR (S)", (161, 98, 7), (202, 138, 4), "sleep"),
            Button(w - 200, h - 70, bw, bh, "CURAR (H)", (21, 128, 61), (22, 163, 74), "heal")
        ]

    def draw_bar(self, screen, x, y, label, val, color):
        """Desenha uma barra de status estilizada com legenda."""
        lbl = self.font_xs.render(label, True, (200, 200, 200))
        screen.blit(lbl, (x, y))
        # Fundo da barra
        pygame.draw.rect(screen, (55, 65, 81), (x, y + 18, 160, 10), border_radius=5)
        # Preenchimento da barra
        fill_width = (val / 100) * 160
        if fill_width > 0:
            pygame.draw.rect(screen, color, (x, y + 18, fill_width, 10), border_radius=5)

    def draw_game_screen(self, screen, pet, mouse_pos):
        """Renderiza todos os elementos da interface de jogo."""
        screen.fill(self.COLOR_BG)
        
        # 1. Painel Superior (Cabeçalho)
        header_rect = pygame.Rect(20, 20, self.w - 40, 80)
        pygame.draw.rect(screen, self.COLOR_PANEL, header_rect, border_radius=15)
        
        name_text = self.font_b.render(pet.name.upper(), True, self.COLOR_BLUE)
        screen.blit(name_text, (40, 35))
        
        lvl_text = self.font_xs.render(f"Nível {pet.level} | {pet.age} dias", True, (156, 163, 175))
        screen.blit(lvl_text, (40, 65))
        
        # Barra de Progresso de XP
        pygame.draw.rect(screen, (17, 24, 39), (self.w - 140, 55, 100, 6), border_radius=3)
        pygame.draw.rect(screen, self.COLOR_BLUE, (self.w - 140, 55, (pet.xp/100)*100, 6), border_radius=3)

        # 2. Área do Pet (Central)
        center_y = self.h // 2 - 80
        pygame.draw.circle(screen, (30, 41, 59), (self.w//2, center_y), 100)
        # Determina o sprite baseado no estado
        sprite_str = "(-_-)zzZ" if pet.is_sleeping else ("( x_x )" if pet.health < 30 else "o( ^-^ )o")
        sprite_font = pygame.font.SysFont("Arial", 48, bold=True)
        sprite_surf = sprite_font.render(sprite_str, True, (255, 255, 255))
        screen.blit(sprite_surf, sprite_surf.get_rect(center=(self.w//2, center_y)))

        # 3. Painel de Status
        status_panel = pygame.Rect(20, self.h // 2 + 30, self.w - 40, 110)
        pygame.draw.rect(screen, self.COLOR_PANEL, status_panel, border_radius=15)
        
        self.draw_bar(screen, 40, self.h // 2 + 45, "FOME", pet.hungry, self.COLOR_RED)
        self.draw_bar(screen, 40, self.h // 2 + 85, "ENERGIA", pet.energy, self.COLOR_YELLOW)
        self.draw_bar(screen, self.w - 200, self.h // 2 + 45, "FELICIDADE", pet.happiness, self.COLOR_BLUE)
        self.draw_bar(screen, self.w - 200, self.h // 2 + 85, "SAÚDE", pet.health, self.COLOR_GREEN)

        # 4. Renderização dos Botões
        for b in self.buttons:
            b.is_hovered = b.rect.collidepoint(mouse_pos)
            b.draw(screen, self.font_s)