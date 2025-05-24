import networkx as nx
import numpy as np

class Grafo:
    def __init__(self):
        # Creamos un grafo no dirigido
        self.grafo = nx.Graph()
        self.ciudades = [
            "BuenosAires", "SaoPaulo", "Lima", "Quito", "Bogota", 
            "CiudadPanama", "SanJose", "Managua", "Tegucigalpa", 
            "SanSalvador", "GuatemalaCity"
        ]
        self.aristas = [
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
        
        self._construir_grafo()

    def _construir_grafo(self):
        # Añadimos los nodos
        self.grafo.add_nodes_from(self.ciudades)
        # Añadimos las aristas con peso
        for u, v, peso in self.aristas:
            self.grafo.add_edge(u, v, weight=peso)

    def mostrar_nodos(self):
        print("Nodos del grafo:")
        print(list(self.grafo.nodes))

    def mostrar_aristas(self):
        print("\nAristas con peso (tiempo):")
        for u, v, data in self.grafo.edges(data=True):
            print(f"{u} <-> {v} : {data['weight']} hrs")

    def floyd_warshall(self):
        # Matriz de distancias mínimas usando algoritmo de Floyd-Warshall de NetworkX
        return dict(nx.floyd_warshall(self.grafo, weight='weight'))

    def imprimir_matriz_distancias(self, matriz):
        print("\nMatriz de distancias mínimas entre ciudades (en horas):")
        ciudades = list(self.grafo.nodes)
        # Cabecera
        print("".ljust(15), end="")
        for c in ciudades:
            print(f"{c.ljust(15)}", end="")
        print()
        
        for origen in ciudades:
            print(f"{origen.ljust(15)}", end="")
            for destino in ciudades:
                dist = matriz[origen][destino]
                if dist == float('inf'):
                    print("∞".ljust(15), end="")
                else:
                    print(f"{dist:.1f}".ljust(15), end="")
            print()

    def calcular_centro(self, matriz_distancias):
        # Excentricidad: máximo de las distancias mínimas desde cada nodo
        excentricidades = {}
        for nodo in self.grafo.nodes:
            distancias = matriz_distancias[nodo].values()
            max_dist = max(distancias)
            excentricidades[nodo] = max_dist

        # Centro = nodo(s) con menor excentricidad
        min_excentricidad = min(excentricidades.values())
        centros = [nodo for nodo, ex in excentricidades.items() if ex == min_excentricidad]
        return centros, min_excentricidad

if __name__ == "__main__":
    grafo = Grafo()
    grafo.mostrar_nodos()
    grafo.mostrar_aristas()
    matriz_distancias = grafo.floyd_warshall()
    grafo.imprimir_matriz_distancias(matriz_distancias)
    centros, excentricidad = grafo.calcular_centro(matriz_distancias)
    print("\nCentro(s) del grafo (nodo(s) con menor distancia máxima a otros nodos):")
    for c in centros:
        print(f"{c} con excentricidad = {excentricidad} hrs")
