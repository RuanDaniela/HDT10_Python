import networkx as nx

def crear_grafo():
    G = nx.DiGraph()  # Grafo dirigido

    # Agregar nodos (ciudades)
    ciudades = [
        "BuenosAires", "SaoPaulo", "Lima", "Quito", "Bogota",
        "CiudadPanama", "SanJose", "Managua", "Tegucigalpa",
        "SanSalvador", "GuatemalaCity"
    ]
    G.add_nodes_from(ciudades)

    # Agregar aristas con pesos (tiempos normales)
    conexiones = [
        ("BuenosAires", "SaoPaulo", 10),
        ("BuenosAires", "Lima", 15),
        ("Lima", "Quito", 10),
        ("Quito", "Bogota", 12),
        ("SaoPaulo", "Bogota", 20),
        ("Bogota", "CiudadPanama", 8),
        ("CiudadPanama", "SanJose", 5),
        ("SanJose", "Managua", 7),
        ("Managua", "Tegucigalpa", 6),
        ("Tegucigalpa", "SanSalvador", 4),
        ("SanSalvador", "GuatemalaCity", 3)
    ]

    for origen, destino, tiempo in conexiones:
        G.add_edge(origen, destino, weight=tiempo)

    return G

if __name__ == "__main__":
    grafo = crear_grafo()
    print("Nodos del grafo:")
    print(grafo.nodes())
    print("\nAristas con peso (tiempo):")
    for u, v, peso in grafo.edges(data='weight'):
        print(f"{u} -> {v} : {peso} hrs")
