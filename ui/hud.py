import pygame

class HUD:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font_large = pygame.font.Font(None, 44)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        
        # Cores
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (220, 50, 50)
        self.GREEN = (50, 200, 50)
        self.BLUE = (50, 100, 200)
        self.YELLOW = (255, 200, 50)
        self.GRAY = (150, 150, 150)

    def draw(self, screen, pet):
        """Desenha a HUD do jogo"""
        # Título e nome do pet
        self._draw_title(screen, pet)
        
        # Stats do pet
        self._draw_stats(screen, pet)
        
        # Barra de saúde
        self._draw_health_bar(screen, pet)
        
        # Instruções de controle
        self._draw_controls(screen)

    def _draw_title(self, screen, pet):
        """Desenha o título e nome do pet"""
        status = "Vivo" if pet.is_alive() else "Morto"
        title = self.font_large.render(f"{pet.name} - Nível {pet.level}", True, self.BLACK)
        title_rect = title.get_rect(center=(self.width // 2, 20))
        screen.blit(title, title_rect)

    def _draw_stats(self, screen, pet):
        """Desenha o status do pet (fome, energia, felicidade)"""
        stats_x = 50
        stats_y = 80
        line_height = 60
        
        # Fome
        self._draw_stat_bar(screen, "Fome", pet.hungry, stats_x, stats_y, self.RED)
        
        # Energia
        self._draw_stat_bar(screen, "Energia", pet.energy, stats_x, stats_y + line_height, self.YELLOW)
        
        # Felicidade
        self._draw_stat_bar(screen, "Felicidade", pet.happiness, stats_x, stats_y + line_height * 2, self.BLUE)
        
        # Saúde
        self._draw_stat_bar(screen, "Saúde", pet.health, stats_x, stats_y + line_height * 3, self.GREEN)
        
        # Escopo do lado direito
        right_x = self.width - 250
        top_y = 100
        
        exp_text = self.font_small.render(f"XP: {pet.experience}/100", True, self.BLACK)
        screen.blit(exp_text, (right_x, top_y))
        
        age_text = self.font_small.render(f"Idade: {pet.age}", True, self.BLACK)
        screen.blit(age_text, (right_x, top_y + 40))

    def _draw_stat_bar(self, screen, label, value, x, y, color):
        """Desenha uma barra de status"""
        label_text = self.font_small.render(label, True, self.BLACK)
        screen.blit(label_text, (x, y))
        
        bar_width = 200
        bar_height = 20
        bar_x = x + 120
        bar_y = y + 5
        
        # Barra de fundo
        pygame.draw.rect(screen, self.GRAY, (bar_x, bar_y, bar_width, bar_height))
        
        # Barra preenchida
        fill_width = (value / 100) * bar_width
        pygame.draw.rect(screen, color, (bar_x, bar_y, fill_width, bar_height))
        
        # Borda
        pygame.draw.rect(screen, self.BLACK, (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Valor em percentual
        value_text = self.font_small.render(f"{int(value)}%", True, self.BLACK)
        value_rect = value_text.get_rect(center=(bar_x + bar_width // 2, bar_y + bar_height // 2))
        screen.blit(value_text, value_rect)

    def _draw_health_bar(self, screen, pet):
        """Desenha a barra de saúde do pet"""
        bar_y = self.height - 100
        bar_width = self.width - 100
        bar_height = 30
        bar_x = 50
        
        # Texto
        health_text = self.font_medium.render("Saúde Geral", True, self.BLACK)
        screen.blit(health_text, (bar_x, bar_y - 40))
        
        # Barra de fundo
        pygame.draw.rect(screen, self.GRAY, (bar_x, bar_y, bar_width, bar_height))
        
        # Barra preenchida (muda de cor dependendo da saúde)
        if pet.health > 50:
            color = self.GREEN
        elif pet.health > 25:
            color = self.YELLOW
        else:
            color = self.RED
        
        fill_width = (pet.health / 100) * bar_width
        pygame.draw.rect(screen, color, (bar_x, bar_y, fill_width, bar_height))
        
        # Borda
        pygame.draw.rect(screen, self.BLACK, (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Valor percentual
        health_value = self.font_medium.render(f"{int(pet.health)}%", True, self.BLACK)
        health_rect = health_value.get_rect(center=(bar_x + bar_width // 2, bar_y + bar_height // 2))
        screen.blit(health_value, health_rect)

    def _draw_controls(self, screen):
        """Desenha as instruções de controle"""
        controls_y = self.height - 30
        controls = [
            "F: Alimentar",
            "P: Brincar",
            "S: Dormir",
            "ESC: Sair"
        ]
        
        for i, control in enumerate(controls):
            x = 50 + (i * 180)
            text = self.font_small.render(control, True, self.BLUE)
            screen.blit(text, (x, controls_y))
