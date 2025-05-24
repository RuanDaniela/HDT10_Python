import networkx as nx

def crear_grafo():
    grafo = nx.DiGraph()

    # Agregar nodos (ciudades)
    ciudades = [
        "BuenosAires", "SaoPaulo", "Lima", "Quito", "Bogota",
        "CiudadPanama", "SanJose", "Managua", "Tegucigalpa",
        "SanSalvador", "GuatemalaCity"
    ]
    grafo.add_nodes_from(ciudades)

    # Agregar aristas con pesos (tiempos en horas)
    aristas = [
        ("BuenosAires", "SaoPaulo", 10),
        ("BuenosAires", "Lima", 15),
        ("SaoPaulo", "Bogota", 20),
        ("Lima", "Quito", 10),
        ("Quito", "Bogota", 12),
        ("Bogota", "CiudadPanama", 8),
        ("CiudadPanama", "SanJose", 5),
        ("SanJose", "Managua", 7),
        ("Managua", "Tegucigalpa", 6),
        ("Tegucigalpa", "SanSalvador", 4),
        ("SanSalvador", "GuatemalaCity", 3)
    ]

    for origen, destino, peso in aristas:
        grafo.add_edge(origen, destino, weight=peso)

    return grafo

def floyd_warshall(grafo):
    # Devuelve un diccionario con la distancia mínima entre cada par de nodos
    return dict(nx.floyd_warshall(grafo, weight='weight'))

def imprimir_matriz_distancias(matriz_distancias):
    nodos = list(matriz_distancias.keys())
    print("\nMatriz de distancias mínimas entre ciudades (en horas):")
    # Imprimir encabezado
    print("\t" + "\t".join(nodos))
    for origen in nodos:
        fila = [origen]
        for destino in nodos:
            dist = matriz_distancias[origen][destino]
            if dist == float('inf'):
                fila.append("∞")
            else:
                fila.append(f"{dist:.1f}")
        print("\t".join(fila))

if __name__ == "__main__":
    grafo = crear_grafo()
    print("Nodos del grafo:")
    print(grafo.nodes())
    print("\nAristas con peso (tiempo):")
    for u, v, peso in grafo.edges(data='weight'):
        print(f"{u} -> {v} : {peso} hrs")

    # Calcular distancias mínimas con Floyd-Warshall
    matriz_distancias = floyd_warshall(grafo)
    imprimir_matriz_distancias(matriz_distancias)
