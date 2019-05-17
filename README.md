# FSI - Práctica 1
El objetivo de esta práctica es comparar los distintos métodos de búsqueda. La diferencia entre los distintos métodos se basa en cómo se añaden los nodos en la lista abierta. Para el caso de de la búsqueda en anchura, la lista abierta es una FIFO. En el caso de la búsqueda en profundidad la lista en una LIFO. La búsqueda de ramificación y acotación (Branch and Bound) se usa una cola ordenada por el coste. Y para la búsqueda de ramificación y acotación con subestimación se usa una cola ordenada por el coste más una heurística. 

Los algoritmos de búsqueda en profundidad y búsqueda en anchura ya estaban realizados. Los que se han implementado han sido el de búsqueda de ramificación y acotación y el búsqueda de ramificación y acotación con subestimación.

A continuación se puede ver algunos recorridos del grafo de las ciudades de Rumanía, y los nodos visitados por cada uno de los métodos de búsqueda.

```
------ RECORRIDO ARAD - BUCHAREST ------
Nodos visitados: 16 
Búsqueda en anchura: [<Node B>, <Node F>, <Node S>, <Node A>]
Nodos visitados: 10 
Búsqueda en Profundidad[<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]
Nodos visitados: 24 
Búsqueda ramificación y acotación[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
Nodos visitados: 6 
Búsqueda ramificación y acotación con subestimación[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]

------ RECORRIDO ORADEA - RIMNICU VILCEA ------
Nodos visitados: 7 
Búsqueda en anchura: [<Node O>, <Node S>, <Node R>]
Nodos visitados: 17 
Búsqueda en Profundidad[<Node O>, <Node S>, <Node A>, <Node T>, <Node L>, <Node M>, <Node D>, <Node C>, <Node P>, <Node R>]
Nodos visitados: 10 
Búsqueda ramificación y acotación[<Node O>, <Node S>, <Node R>]
Nodos visitados: 3 
Búsqueda ramificación y acotación con subestimación[<Node O>, <Node S>, <Node R>]

------ RECORRIDO SIBIU - BUCHAREST ------
Nodos visitados: 10 
Búsqueda en anchura: [<Node B>, <Node F>, <Node S>]
Nodos visitados: 23 
Búsqueda en Profundidad[<Node B>, <Node P>, <Node R>, <Node S>]
Nodos visitados: 14 
Búsqueda ramificación y acotación[<Node B>, <Node P>, <Node R>, <Node S>]
Nodos visitados: 5 
Búsqueda ramificación y acotación con subestimación[<Node B>, <Node P>, <Node R>, <Node S>]

------ RECORRIDO TIMISOARA - PITESTI ------
Nodos visitados: 23 
Búsqueda en anchura: [<Node P>, <Node R>, <Node S>, <Node A>, <Node T>]
Nodos visitados: 7 
Búsqueda en Profundidad[<Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>]
Nodos visitados: 22 
Búsqueda ramificación y acotación[<Node P>, <Node R>, <Node S>, <Node A>, <Node T>]
Nodos visitados: 9 
Búsqueda ramificación y acotación con subestimación[<Node P>, <Node R>, <Node S>, <Node A>, <Node T>]

------ RECORRIDO VASLUI - CRAIOVA ------
Nodos visitados: 18 
Búsqueda en anchura: [<Node C>, <Node P>, <Node B>, <Node U>, <Node V>]
Nodos visitados: 13 
Búsqueda en Profundidad[<Node C>, <Node P>, <Node R>, <Node S>, <Node F>, <Node B>, <Node U>, <Node V>]
Nodos visitados: 20 
Búsqueda ramificación y acotación[<Node C>, <Node P>, <Node B>, <Node U>, <Node V>]
Nodos visitados: 7 
Búsqueda ramificación y acotación con subestimación[<Node C>, <Node P>, <Node B>, <Node U>, <Node V>]

------ RECORRIDO ZERIND - URZICENI ------
Nodos visitados: 22 
Búsqueda en anchura: [<Node U>, <Node B>, <Node F>, <Node S>, <Node A>, <Node Z>]
Nodos visitados: 28 
Búsqueda en Profundidad[<Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>, <Node Z>]
Nodos visitados: 30 
Búsqueda ramificación y acotación[<Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>, <Node Z>]
Nodos visitados: 13 
Búsqueda ramificación y acotación con subestimación[<Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>, <Node Z>]

```
Como se puede ver, el algoritmo con mejores resultados es el de ramificación y acotación con subestimación. Desatacar que aunque los algoritmos de búsqueda en anchura y profundidad den con una solución, no significa que esta sea óptima ya que aunque tenga menor número de nodos su coste puede ser mayor. Mientras que con ramificación y acotación, y ramificación y acotación con subestimación sí se llega a una solución óptima. Además con ramificación y acotación con subestimación se visita un menor número de nodos.
