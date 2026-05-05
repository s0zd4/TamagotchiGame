import pygame
import sys
from pet.pet import Pet
from ui.hud import HUD

class Game:
    def __init__(self):
        pygame.init()
        # Dimensões verticais inspiradas em dispositivos móveis
        self.WIDTH, self.HEIGHT = 420, 760
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tamagotchi Virtual")
        self.clock = pygame.time.Clock()
        self.hud = HUD(self.WIDTH, self.HEIGHT)
        
        # Tenta carregar pet existente
        self.pet = Pet.load()
        self.state = "PLAYING" if self.pet else "START"
        self.input_name = ""
        
        # Evento temporizador para a passagem do tempo (a cada 2 segundos)
        self.TICK_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TICK_EVENT, 2000)

    def run(self):
        """Ciclo principal de execução."""
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.pet: self.pet.save()
                    pygame.quit(); sys.exit()
                
                if self.state == "START":
                    self.handle_start_logic(event)
                elif self.state == "PLAYING":
                    self.handle_game_logic(event, mouse_pos)

            self.render(mouse_pos)
            self.clock.tick(60)

    def handle_start_logic(self, event):
        """Gere a entrada de texto na tela inicial."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.input_name:
                self.pet = Pet(self.input_name)
                self.pet.save()
                self.state = "PLAYING"
            elif event.key == pygame.K_BACKSPACE:
                self.input_name = self.input_name[:-1]
            else:
                if len(self.input_name) < 12 and event.unicode.isalnum():
                    self.input_name += event.unicode

    def handle_game_logic(self, event, mouse_pos):
        """Gere os eventos durante a jogabilidade."""
        if not self.pet.is_alive(): return
        
        if event.type == self.TICK_EVENT:
            self.pet.pass_time()
            self.pet.save() # Auto-save a cada alteração temporal

        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in self.hud.buttons:
                if b.rect.collidepoint(mouse_pos):
                    self.process_action(b.action)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f: self.pet.feed()
            if event.key == pygame.K_p: self.pet.play()
            if event.key == pygame.K_s: self.pet.sleep_toggle()
            if event.key == pygame.K_h: self.pet.heal()

    def process_action(self, action):
        """Executa a ação correspondente do pet."""
        if action == "feed": self.pet.feed()
        elif action == "play": self.pet.play()
        elif action == "sleep": self.pet.sleep_toggle()
        elif action == "heal": self.pet.heal()

    def render(self, mouse_pos):
        """Trata do desenho dos estados do jogo."""
        if self.state == "START":
            self.screen.fill((31, 41, 55))
            f = pygame.font.SysFont("Arial", 24, bold=True)
            t = f.render("NOME DO TEU NOVO PET:", True, (255, 255, 255))
            self.screen.blit(t, (self.WIDTH//2 - t.get_width()//2, 250))
            
            # Caixa de Entrada Visual
            pygame.draw.rect(self.screen, (55, 65, 81), (60, 300, 300, 50), border_radius=10)
            txt_surf = f.render(self.input_name + "|", True, (59, 130, 246))
            self.screen.blit(txt_surf, (self.WIDTH//2 - txt_surf.get_width()//2, 310))
            
        elif self.state == "PLAYING":
            if not self.pet.is_alive():
                self.render_death_screen()
            else:
                self.hud.draw_game_screen(self.screen, self.pet, mouse_pos)
        
        pygame.display.flip()

    def render_death_screen(self):
        """Desenha a tela de fim de jogo."""
        self.screen.fill((20, 0, 0))
        m_font = pygame.font.SysFont("Arial", 40, True)
        m_surf = m_font.render("O PET MORREU", True, (220, 38, 38))
        self.screen.blit(m_surf, (self.WIDTH//2 - m_surf.get_width()//2, self.HEIGHT//2))