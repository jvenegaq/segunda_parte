import sqlite3

def crear_tabla():
    conn = sqlite3.connect('base_solucion1.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

crear_tabla()
print("Tabla 'equipos' creada exitosamente.")
