import sqlite3
import os

def limpar_banco():
    caminho_db = os.path.join('db', 'pet_info.db')
    
    if not os.path.exists(caminho_db):
        print("O arquivo de banco de dados não foi encontrado. Nada para limpar.")
        return

    try:
        conn = sqlite3.connect(caminho_db)
        cursor = conn.cursor()
        
        # Apaga todos os registros da tabela pet_status
        cursor.execute("DELETE FROM pet_status")
        
        # Opcional: Reseta o contador de IDs autoincrement
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='pet_status'")
        
        conn.commit()
        conn.close()
        print("Sucesso! Os dados do pet antigo foram removidos.")
        print("Agora, ao iniciar o jogo, você poderá criar um novo pet.")
    except Exception as e:
        print(f"Ocorreu um erro ao limpar o banco: {e}")

if __name__ == "__main__":
    confirmacao = input("Tem certeza que deseja apagar o pet atual? (s/n): ")
    if confirmacao.lower() == 's':
        limpar_banco()
    else:
        print("Operação cancelada.")