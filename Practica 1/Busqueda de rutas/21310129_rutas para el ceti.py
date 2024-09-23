"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
"""

from collections import deque

def bfs_rutas(grafo, inicio, fin):
    """
    Encuentra todas las rutas posibles desde el nodo 'inicio' hasta el nodo 'fin' usando BFS.
    :param grafo: Diccionario que representa el grafo.
    :param inicio: Nodo de inicio.
    :param fin: Nodo objetivo.
    :return: Lista de rutas posibles.
    """
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
    'Casa': ['Tren'],
    'Tren': ['PlazaPatria', 'Camion'],
    'PlazaPatria': ['Tren', 'Camion'],
    'Camion': ['Tren','PlazaPatria','Heladeria'],
    'Heladeria': ['Camion', 'Ceti'],
    'Ceti': ['Heladeria']
}
inicio = 'Casa'
fin = 'Ceti'
rutas = bfs_rutas(grafo, inicio, fin)
print(f"Rutas desde {inicio} a {fin}: {rutas}")

"Preguntar por que te sale mal al cambiar del grafo ya sea A o F a casa o ceti por que te sale un error de KeyError"