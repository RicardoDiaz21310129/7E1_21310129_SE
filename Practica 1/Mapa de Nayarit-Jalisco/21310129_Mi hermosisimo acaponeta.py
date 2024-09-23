"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
"""

from collections import deque

def bfs_rutas(grafo, inicio, fin):
    rutas = []
    cola = deque([(inicio, [inicio])])  # (nodo actual, ruta actual)

    while cola:
        nodo_actual, ruta_actual = cola.popleft()
        if nodo_actual == fin:
            rutas.append(ruta_actual)
        else:
            for vecino in grafo[nodo_actual]:
                if vecino not in ruta_actual:
                    cola.append((vecino, ruta_actual + [vecino]))
    
    return rutas

# Ejemplo de uso
grafo = {
    'Acaponeta': ['Tecuala', 'Tepic'],
    'Tecuala': ['Acaponeta', 'Tepic', 'Novillero'],
    'Tepic': ['Acaponeta', 'Tecuala', 'Gdl'],
    'Gdl': ['Tepic'],
    'Novillero': ['Tecuala'],
}
inicio = 'Acaponeta'
fin = 'Novillero'
rutas = bfs_rutas(grafo, inicio, fin)
print(f"Rutas desde {inicio} a {fin}: {rutas}")