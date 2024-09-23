"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
"""

def dfs_tareas(grafo, tarea, visitado=None, orden=None):

    if visitado is None:
        visitado = set()
    if orden is None:
        orden = []
    
    visitado.add(tarea)
    for vecino in grafo[tarea]:
        if vecino not in visitado:
            dfs_tareas(grafo, vecino, visitado, orden)
    orden.append(tarea)
    
    return orden

# Ejemplo de uso
grafo = {
    'Proyect1': ['Proyect4', 'Proyect2'],
    'Proyect2': ['Proyect3'],
    'Proyect3': [],
    'Proyect4': []
}
inicio = 'Proyect1'
orden = dfs_tareas(grafo, inicio)
print(f"Orden de ejecución de las tareas: {orden[::-1]}")