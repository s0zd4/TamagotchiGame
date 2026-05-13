import sys
import os

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import atualizar_pet

class Pet:
    def __init__(self, name, hungry=0, happiness=100, energy=100, health=100, experience=0, level=1, age=0):
        self.name = name
        self.hungry = hungry
        self.happiness = happiness
        self.energy = energy
        self.health = health
        self.experience = experience
        self.level = level
        self.age = age
        self.is_sleeping = False  # Estado de sono do pet

    def atualizar_estado(self):
        """Atualiza os dados do pet atual no banco de dados."""
        atualizar_pet(self.name, self.hungry, self.happiness, self.energy, 
                     self.health, self.experience, self.level, self.age)
        
    def feed(self):
        """Alimenta o pet, reduz fome e restaura um pouco de energia"""
        if self.is_sleeping:
            return  # Não permite alimentar enquanto dormindo
            
        if self.hungry > 0:
            self.hungry = max(0, self.hungry - 30)
            self.energy = min(100, self.energy + 2)  # Pequena recuperação de energia ao comer
            self.happiness = min(100, self.happiness + 5)
            self.health = min(100, self.health + 10)
        else:
            self.health = max(0, self.health - 10)
        
        self.atualizar_estado()

    def play(self):
        """Pet brinca, fica feliz, mas gasta energia e fica com fome"""
        if self.is_sleeping:
            return  # Não permite brincar enquanto dormindo
            
        if self.energy >= 20:
            self.hungry = min(100, self.hungry + 20)  # Aumenta mais fome ao brincar
            self.energy = max(0, self.energy - 20)  # Gasta energia ao brincar
            self.happiness = min(100, self.happiness + 25)
            self.experience += 10
            self._check_level_up()
        else:
            self.happiness = max(0, self.happiness - 10)
        
        self.atualizar_estado()

    def toggle_sleep(self):
        """Alterna o estado de sono do pet."""
        self.is_sleeping = not self.is_sleeping
        if self.is_sleeping:
            self.energy = min(100, self.energy + 20)  # Pequena recuperação ao dormir
        else:
            self.happiness = max(0, self.happiness - 5)  # Perde felicidade ao acordar
        
        self.atualizar_estado()

    def heal(self):
        """Cura o pet recuperando saúde."""
        if self.is_sleeping:
            return  # Não permite curar enquanto dormindo
            
        if self.health < 100:
            self.health = min(100, self.health + 25)
            self.happiness = min(100, self.happiness + 5)
            self.energy = min(100, self.energy + 5)
        
        self.atualizar_estado()

    def update_needs(self):
        """Atualiza as necessidades do pet (fome, energia, felicidade, saúde)"""
        if self.is_sleeping:
            # Quando dormindo, regenera energia constantemente
            self.energy = min(100, self.energy + 5)
            # Pequena recuperação de saúde durante o sono
            self.health = min(100, self.health + 1)
        else:
            # Quando acordado, necessidades normais
            self.hungry = min(100, self.hungry + 3)
            self.energy = max(0, self.energy - 2)
            self.happiness = max(0, self.happiness - 2)
            self.health = max(0, self.health - 1)
        
        self._check_health()

    def age_up(self):
        """Aumenta a idade do pet"""
        self.age += 1

    def update(self, needs_counter, age_counter):
        """Atualiza o pet baseado nos contadores de tempo."""
        updated = False
        
        if needs_counter >= 5:  # Atualiza necessidades a cada 5 segundos
            self.update_needs()
            updated = True
        
        if age_counter >= 10:  # Envelhece a cada 10 segundos
            self.age_up()
            updated = True
        
        # Salva no banco se houve atualização
        if updated:
            self.atualizar_estado()

    def _check_health(self):
        """Verifica a saúde do pet baseado no estado"""
        if self.hungry > 80:
            self.health = max(0, self.health - 5)
        if self.energy < 20:
            self.health = max(0, self.health - 3)
        if self.happiness < 20:
            self.health = max(0, self.health - 2)

    def _check_level_up(self):
        """Verifica se o pet sobe de nível"""
        if self.experience >= 100:
            self.level += 1
            self.experience = 0
            self.happiness = min(100, self.happiness + 10)
            self.health = min(100, self.health + 20)

    def get_status(self):
        """Retorna um dicionário com o status atual do pet"""
        return {
            'name': self.name,
            'level': self.level,
            'hungry': self.hungry,
            'energy': self.energy,
            'happiness': self.happiness,
            'health': self.health,
            'experience': self.experience,
            'age': self.age
        }

    def is_alive(self):
        """Verifica se o pet ainda está vivo"""
        return self.health > 0 #Medo disso ficar -1 x_x
