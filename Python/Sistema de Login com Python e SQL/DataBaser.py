import sqlite3

# Criar conexão com o banco
conectar = sqlite3.connect("UsuariosDATA.db")
cursor = conectar.cursor()

# Criar a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_Usuarios (
    Id_Usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Usuario TEXT NOT NULL,
    Senha TEXT NOT NULL 
);
""")

print("Conectado ao Banco de Dados, TÁ SUAVE")

