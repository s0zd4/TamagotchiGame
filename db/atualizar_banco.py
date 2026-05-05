import sqlite3
import os

def configurar_e_verificar_banco():
    # Caminho do banco conforme a estrutura do seu repositório
    caminho_db = os.path.join('db', 'pet_info.db')
    
    # Garante que a pasta db existe
    if not os.path.exists('db'):
        os.makedirs('db')
        print("Pasta 'db' criada.")

    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    # 1. Criar a tabela inicial se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pet_status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # 2. Adicionar as colunas de estado (uma por uma para evitar erro se já existirem)
    colunas = [
        ("hungry", "INTEGER DEFAULT 100"),
        ("happiness", "INTEGER DEFAULT 100"),
        ("energy", "INTEGER DEFAULT 100"),
        ("health", "INTEGER DEFAULT 100"),
        ("experience", "INTEGER DEFAULT 0"),
        ("level", "INTEGER DEFAULT 1"),
        ("age", "INTEGER DEFAULT 0")
    ]

    for nome_col, definicao in colunas:
        try:
            cursor.execute(f"ALTER TABLE pet_status ADD COLUMN {nome_col} {definicao}")
            print(f"Coluna '{nome_col}' adicionada.")
        except sqlite3.OperationalError:
            print(f"Coluna '{nome_col}' já existe.")

    conn.commit()

    # 3. VERIFICAÇÃO FINAL: Mostrar a estrutura da tabela
    print("\n--- ESTRUTURA ATUAL DA TABELA 'pet_status' ---")
    cursor.execute("PRAGMA table_info(pet_status)")
    colunas_reais = cursor.fetchall()
    
    for c in colunas_reais:
        # c[1] é o nome da coluna, c[2] é o tipo
        print(f"Campo: {c[1]} | Tipo: {c[2]}")
    
    print("----------------------------------------------")
    
    conn.close()

if __name__ == "__main__":
    configurar_e_verificar_banco()