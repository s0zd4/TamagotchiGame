import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hungry = 50
        self.energy = 50
        self.happiness = 50
        self.level = 1
        self.experience = 0
        self.is_sleeping = False
        self.health = 100
        self.age = 0
        
    def feed(self):
        """Alimenta o pet, reduz fome e restaura um pouco de energia"""
        if self.hungry > 0:
            self.hungry = max(0, self.hungry - 30)
            self.energy = min(100, self.energy + 10)  # Pequena recuperação de energia ao comer
            self.happiness = min(100, self.happiness + 5)
            self.health = min(100, self.health + 10)
        else:
            self.health = max(0, self.health - 10)

    def play(self):
        """Pet brinca, fica feliz, mas gasta energia e fica com fome"""
        if self.energy >= 20:
            self.hungry = min(100, self.hungry + 20)  # Aumenta mais fome ao brincar
            self.energy = max(0, self.energy - 20)  # Gasta energia ao brincar
            self.happiness = min(100, self.happiness + 25)
            self.experience += 10
            self._check_level_up()
        else:
            self.happiness = max(0, self.happiness - 10)

    def sleep(self):
        """Pet dorme e recupera muita energia"""
        self.is_sleeping = True
        self.energy = min(100, self.energy + 40)  # Grande recuperação de energia
        self.happiness = max(0, self.happiness - 5)  # Perde um pouco de felicidade
        self.is_sleeping = False

    def pass_time(self):
        """Passa o tempo e reduz atributos naturalmente"""
        if not self.is_sleeping:
            self.hungry = min(100, self.hungry + 3)
            self.energy = max(0, self.energy - 2)
            self.happiness = max(0, self.happiness - 2)
            self.health = max(0, self.health - 1)
        
        self.age += 1
        self._check_health()

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
        return self.health > 0
