import sqlite3
import os

DB_PATH = os.path.join('db', 'pet_info.db')

def inicializar_banco():
    """Cria o banco de dados e a tabela se não existirem."""
    if not os.path.exists('db'):
        os.makedirs('db')
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Criar tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pet_status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            hungry INTEGER DEFAULT 100,
            happiness INTEGER DEFAULT 100,
            energy INTEGER DEFAULT 100,
            health INTEGER DEFAULT 100,
            experience INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            age INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def pet_existe():
    """Verifica se um pet já foi criado."""
    inicializar_banco()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pet_status")
    resultado = cursor.fetchone()[0]
    conn.close()
    return resultado > 0

def carregar_pet():
    """Carrega o pet do banco de dados (retorna o primeiro/único pet)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, hungry, happiness, energy, health, experience, level, age 
        FROM pet_status LIMIT 1
    """)
    dados = cursor.fetchone()
    conn.close()
    
    if dados:
        return dados
    return None

def criar_novo_pet(nome):
    """Cria um novo pet no banco de dados."""
    inicializar_banco()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Primeiro, limpar dados antigos se existirem
        cursor.execute("DELETE FROM pet_status")
        
        # Inserir novo pet
        cursor.execute('''
            INSERT INTO pet_status (name, hungry, happiness, energy, health, experience, level, age)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, 100, 100, 100, 100, 0, 1, 0))
        
        conn.commit()
        print(f"Pet '{nome}' criado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao criar pet: {e}")
        return False
    finally:
        conn.close()

def atualizar_pet(nome, hungry, happiness, energy, health, experience, level, age):
    """Atualiza os dados do pet no banco de dados."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            UPDATE pet_status SET 
            hungry = ?, happiness = ?, energy = ?, health = ?, 
            experience = ?, level = ?, age = ?, last_updated = CURRENT_TIMESTAMP
            WHERE name = ?
        ''', (hungry, happiness, energy, health, experience, level, age, nome))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar pet: {e}")
    finally:
        conn.close()
