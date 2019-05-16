# Search methods

import search

#ab = search.GPSProblem('SA', 'NT' , search.australia)
ab = search.GPSProblem('A', 'B', search.romania)
ro = search.GPSProblem('R', 'O', search.romania)
sb = search.GPSProblem('S', 'B', search.romania)
tp = search.GPSProblem('T', 'P', search.romania)
vc = search.GPSProblem('V', 'C', search.romania)
zu = search.GPSProblem('Z', 'U', search.romania)

print("------ RECORRIDO ARAD - BUCHAREST ------")
print("Búsqueda en anchura: " + str(search.breadth_first_graph_search(ab).path())) #Anchura
print("Búsqueda en Profundidad" +str(search.depth_first_graph_search(ab).path()))  #Profundidad
print("Búsqueda ramificación y acotación" +str(search.ramificacion_acotacion(ab).path())) #ramificacion y acotacion.
print("Búsqueda ramificación y acotación con subestimación" + str(search.ramificacion_subestimacion(ab).path()))

print("\n------ RECORRIDO ORADEA - RIMNICU VILCEA ------")
print("Búsqueda en anchura: " + str(search.breadth_first_graph_search(ro).path())) #Anchura
print("Búsqueda en Profundidad" +str(search.depth_first_graph_search(ro).path()))  #Profundidad
print("Búsqueda ramificación y acotación" +str(search.ramificacion_acotacion(ro).path())) #ramificacion y acotacion.
print("Búsqueda ramificación y acotación con subestimación" + str(search.ramificacion_subestimacion(ro).path()))

print("\n------ RECORRIDO SIBIU - BUCHAREST ------")
print("Búsqueda en anchura: " + str(search.breadth_first_graph_search(sb).path())) #Anchura
print("Búsqueda en Profundidad" +str(search.depth_first_graph_search(sb).path()))  #Profundidad
print("Búsqueda ramificación y acotación" +str(search.ramificacion_acotacion(sb).path())) #ramificacion y acotacion.
print("Búsqueda ramificación y acotación con subestimación" + str(search.ramificacion_subestimacion(sb).path()))

print("\n------ RECORRIDO TIMISOARA - PITESTI ------")
print("Búsqueda en anchura: " + str(search.breadth_first_graph_search(tp).path())) #Anchura
print("Búsqueda en Profundidad" +str(search.depth_first_graph_search(tp).path()))  #Profundidad
print("Búsqueda ramificación y acotación" +str(search.ramificacion_acotacion(tp).path())) #ramificacion y acotacion.
print("Búsqueda ramificación y acotación con subestimación" + str(search.ramificacion_subestimacion(tp).path()))

print("\n------ RECORRIDO VASLUI - CRAIOVA ------")
print("Búsqueda en anchura: " + str(search.breadth_first_graph_search(vc).path())) #Anchura
print("Búsqueda en Profundidad" +str(search.depth_first_graph_search(vc).path()))  #Profundidad
print("Búsqueda ramificación y acotación" +str(search.ramificacion_acotacion(vc).path())) #ramificacion y acotacion.
print("Búsqueda ramificación y acotación con subestimación" + str(search.ramificacion_subestimacion(vc).path()))

print("\n------ RECORRIDO ZERIND - URZICENI ------")
print("Búsqueda en anchura: " + str(search.breadth_first_graph_search(zu).path())) #Anchura
print("Búsqueda en Profundidad" +str(search.depth_first_graph_search(zu).path()))  #Profundidad
print("Búsqueda ramificación y acotación" +str(search.ramificacion_acotacion(zu).path())) #ramificacion y acotacion.
print("Búsqueda ramificación y acotación con subestimación" + str(search.ramificacion_subestimacion(zu).path()))

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
