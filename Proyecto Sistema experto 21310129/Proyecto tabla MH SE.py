import sqlite3

# Conectar a la base de datos (se crea un archivo .db si no existe)
conn = sqlite3.connect('monster_hunter.db')
cursor = conn.cursor()

# Crear la tabla Monsters
cursor.execute('''
CREATE TABLE IF NOT EXISTS Monsters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    weakness TEXT,
    resistance TEXT
)
''')

# Insertar datos en la tabla
cursor.executemany('''
INSERT INTO Monsters (name, type, weakness, resistance) VALUES (?, ?, ?, ?)
''', [
('Rathalos', 'Fuego', 'Agua', 'Fuego'),
('Zinogre', 'Trueno', 'Hielo', 'Trueno'),
('Anjanath', 'Fuego', 'Agua', 'Fuego'),
('Nergigante', 'Dragón', 'Rayo', 'Dragón'),
('Barioth', 'Hielo', 'Fuego', 'Hielo'),
('Rathian', 'Veneno/Fuego', 'Dragón', 'Fuego'),
('Tigrex', 'Bestia Voladora', 'Trueno', 'Hielo'),
('Diablos', 'Tierra', 'Hielo', 'Fuego'),
('Kushala Daora', 'Viento', 'Trueno', 'Agua'),
('Teostra', 'Fuego/Explosivo', 'Agua', 'Fuego'),
('Legiana', 'Hielo', 'Trueno', 'Hielo'),
('Pukei-Pukei', 'Veneno', 'Rayo', 'Agua'),
('Tobi-Kadachi', 'Trueno', 'Agua', 'Rayo'),
('Kirin', 'Trueno', 'Fuego', 'Rayo'),
('Velkhana', 'Hielo', 'Fuego', 'Hielo'),
('Brachydios', 'Explosivo', 'Agua', 'Explosión'),
('Glavenus', 'Fuego', 'Agua', 'Fuego'),
('Alatreon', 'Dragón/Elemental', 'Depende del estado', 'Fuego/Hielo'),
('Rajang', 'Trueno', 'Hielo', 'Trueno'),
('Bazelgeuse', 'Explosivo', 'Hielo', 'Fuego'),
]);

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Tabla creada y datos insertados correctamente.")
