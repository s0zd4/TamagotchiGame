import pygame

class Button:
    def __init__(self, x, y, w, h, text, color, hover_color, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.disabled_color = (64, 64, 64)  # Cor quando desabilitado
        self.action = action
        self.is_hovered = False
        self.is_pressed = False
        self.disabled = False

    def draw(self, screen, font):
        # Ajusta posição baseado no estado pressionado
        draw_rect = self.rect.copy()
        if self.is_pressed and not self.disabled:
            draw_rect.y += 2
        
        # Efeito de sombra para profundidade
        shadow_rect = draw_rect.copy()
        shadow_rect.y += 4
        pygame.draw.rect(screen, (15, 23, 42), shadow_rect, border_radius=12)
        
        # Desenha o botão principal
        if self.disabled:
            current_color = self.disabled_color
        else:
            current_color = self.hover_color if self.is_hovered else self.color
            
        pygame.draw.rect(screen, current_color, draw_rect, border_radius=12)
        pygame.draw.rect(screen, (255, 255, 255), draw_rect, 2, border_radius=12)
        
        # Texto do botão (cinza quando desabilitado)
        text_color = (128, 128, 128) if self.disabled else (255, 255, 255)
        txt_surf = font.render(self.text, True, text_color)
        screen.blit(txt_surf, txt_surf.get_rect(center=draw_rect.center))

class HUD:
    def __init__(self, w, h):
        self.w, self.h = w, h
        # Paleta de Cores "Dark Theme" similar ao HTML
        self.COLOR_BG = (15, 23, 42)  # slate-900
        self.COLOR_PANEL = (30, 41, 59)  # slate-700
        self.COLOR_BLUE = (59, 130, 246)  # blue-500
        self.COLOR_RED = (239, 68, 68)  # red-500
        self.COLOR_YELLOW = (245, 158, 11)  # amber-500
        self.COLOR_GREEN = (34, 197, 94)  # green-500
        
        # Tentar carregar fonte pixel, senão usar Arial
        try:
            self.font_pixel = pygame.font.Font("assets/fonts/pixel.ttf", 24)
        except:
            self.font_pixel = pygame.font.SysFont("Courier New", 24, bold=True)
        
        self.font_b = pygame.font.SysFont("Arial", 22, bold=True)
        self.font_s = pygame.font.SysFont("Arial", 14, bold=True)
        self.font_xs = pygame.font.SysFont("Arial", 12)

        # Animação do sprite
        self.sprite_bounce = 0
        self.sprite_direction = 1
        
        # Valores exibidos com animação suave
        self.displayed_hungry = 100
        self.displayed_energy = 100
        self.displayed_happiness = 100
        self.displayed_health = 100
        self.displayed_xp = 0
        
        # Configuração dos Botões de Ação
        bw, bh = 170, 50
        self.buttons = [
            Button(30, h - 130, bw, bh, "ALIMENTAR (F)", (185, 28, 28), (220, 38, 38), "feed"),
            Button(w - 200, h - 130, bw, bh, "BRINCAR (P)", (29, 78, 216), (59, 130, 246), "play"),
            Button(30, h - 70, bw, bh, "DORMIR (S)", (161, 98, 7), (202, 138, 4), "sleep"),
            Button(w - 200, h - 70, bw, bh, "CURAR (H)", (21, 128, 61), (22, 163, 74), "heal")
        ]

    def draw_bar(self, screen, x, y, label, val, color):
        """Desenha uma barra de status estilizada com legenda e valor percentual."""
        # Label da barra
        lbl = self.font_xs.render(label, True, (200, 200, 200))
        screen.blit(lbl, (x, y))
        
        # Valor percentual
        val_text = self.font_xs.render(f"{int(val)}%", True, (255, 255, 255))
        screen.blit(val_text, (x + 140, y))
        
        # Fundo da barra
        pygame.draw.rect(screen, (55, 65, 81), (x, y + 18, 160, 12), border_radius=6)
        # Preenchimento da barra
        fill_width = (val / 100) * 160
        if fill_width > 0:
            pygame.draw.rect(screen, color, (x, y + 18, fill_width, 12), border_radius=6)

    def draw_game_screen(self, screen, pet, mouse_pos, mouse_pressed):
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
        pygame.draw.rect(screen, self.COLOR_BLUE, (self.w - 140, 55, (self.displayed_xp/100)*100, 6), border_radius=3)

        # 2. Área do Pet (Central)
        center_y = self.h // 2 - 80
        # Animação de bounce
        self.sprite_bounce += self.sprite_direction * 0.5
        if self.sprite_bounce > 5 or self.sprite_bounce < -5:
            self.sprite_direction *= -1
        
        pet_y = center_y + self.sprite_bounce
        
        # Círculo de fundo do pet
        pygame.draw.circle(screen, (30, 41, 59), (self.w//2, center_y), 100)
        
        # Determina o sprite baseado no estado
        if pet.is_sleeping:
            sprite_str = "(-_-)zzZ"
        elif pet.health < 30:
            sprite_str = "(x_x)"
        else:
            sprite_str = "o(^_^)o"
        
        # Renderiza sprite com fonte pixel
        sprite_surf = self.font_pixel.render(sprite_str, True, (255, 255, 255))
        screen.blit(sprite_surf, sprite_surf.get_rect(center=(self.w//2, pet_y)))

        # 3. Painel de Status
        status_panel = pygame.Rect(20, self.h // 2 + 30, self.w - 40, 110)
        pygame.draw.rect(screen, self.COLOR_PANEL, status_panel, border_radius=15)
        
        self.draw_bar(screen, 40, self.h // 2 + 45, "FOME", self.displayed_hungry, self.COLOR_RED)
        self.draw_bar(screen, 40, self.h // 2 + 85, "ENERGIA", self.displayed_energy, self.COLOR_YELLOW)
        self.draw_bar(screen, self.w - 200, self.h // 2 + 45, "FELICIDADE", self.displayed_happiness, self.COLOR_BLUE)
        self.draw_bar(screen, self.w - 200, self.h // 2 + 85, "SAÚDE", self.displayed_health, self.COLOR_GREEN)

        # 4. Renderização dos Botões
        for b in self.buttons:
            # Desabilita botões quando o pet está dormindo (exceto o botão de dormir)
            b.disabled = pet.is_sleeping and b.action != "sleep"
            b.is_hovered = b.rect.collidepoint(mouse_pos) and not b.disabled
            if mouse_pressed and b.is_hovered:
                b.is_pressed = True
            else:
                b.is_pressed = False
            b.draw(screen, self.font_s)

    def update_displayed_stats(self, pet):
        """Atualiza os valores exibidos com animação suave"""
        # Taxa de interpolação (quanto maior, mais rápida a animação)
        lerp_speed = 0.05
        
        # Interpola cada status para o valor real
        self.displayed_hungry += (pet.hungry - self.displayed_hungry) * lerp_speed
        self.displayed_energy += (pet.energy - self.displayed_energy) * lerp_speed
        self.displayed_happiness += (pet.happiness - self.displayed_happiness) * lerp_speed
        self.displayed_health += (pet.health - self.displayed_health) * lerp_speed
        self.displayed_xp += (pet.experience - self.displayed_xp) * lerp_speed