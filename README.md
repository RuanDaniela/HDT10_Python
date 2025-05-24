Proyecto Grafo con Algoritmo de Floyd-Warshall en Python
Descripción
Este proyecto implementa un grafo dirigido no dirigido que representa un conjunto de ciudades conectadas por rutas con pesos que indican tiempos de viaje en horas. Utilizamos la biblioteca NetworkX para facilitar la creación y manejo del grafo, y aplicamos el algoritmo de Floyd-Warshall para calcular las distancias mínimas entre todos los pares de ciudades.

Además, calculamos el centro del grafo, definido como el nodo con la menor excentricidad (es decir, el nodo cuya distancia máxima a cualquier otro nodo es mínima), lo que puede interpretarse como la ciudad mejor posicionada para minimizar el tiempo máximo de viaje a cualquier otra ciudad.

Contenido principal
Clase Grafo que:

Construye el grafo no dirigido con las ciudades y sus conexiones (aristas con pesos).

Muestra los nodos y las aristas con sus pesos.

Calcula la matriz de distancias mínimas entre todos los nodos usando el algoritmo de Floyd-Warshall.

Imprime la matriz de distancias de forma ordenada.

Calcula y muestra el centro del grafo basado en la excentricidad.

Tecnologías y librerías
Lenguaje: Python 3

Librería: NetworkX

Uso
Clonar el repositorio o descargar los archivos.

Instalar NetworkX con:

bash
Copiar
Editar
pip install networkx
Ejecutar el programa principal con:

bash
Copiar
Editar
python3 grafo.py
Observar la salida que incluye:

Listado de nodos y aristas con sus pesos.

Matriz de distancias mínimas entre todas las ciudades.

Centro(s) del grafo con su excentricidad.

Nota
Esta implementación se realizó con la ayuda de ChatGPT, un asistente de inteligencia artificial desarrollado por OpenAI, quien colaboró en el diseño, explicación y mejora del código.

