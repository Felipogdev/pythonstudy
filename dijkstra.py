import heapq

def dijkstra(start, target, graph):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n  # Para rastrear o caminho
    dist[start] = 0
    pq = []  # Priority queue
    heapq.heappush(pq, (0, start))

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))

    # Reconstruir o caminho
    path = []
    at = target
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()

    return dist[target], path

def main():
    graph = {
[(1,240),(2,180),(3,120)]#Vertice 0(Start)
[(0,240),(12,30),(4,35),(5,35),(6,35)]#Vertice 1(Filmes)
[(0,180),(8,25),(9,25),(7,25),(6,30)]#Vertice 2(Jogos)
[(),(),(),(),()]#Vertice 3(Fotografia)
[]#Vertice 4(Ação)
[]#Vertice 5(Terror)
[]#Vertice 6(Aventura)
[]#Vertice 7(PvP)
[]#Vertice 8(Open World)
[]#Vertice 9(SinglePlayer)
[]#Vertice 10(Plantas)
[]#Vertice 11(Paisagens)
[]#Vertice 12(Carros)
[]#Vertice 13(Filipa)
[]#Vertice 14(Mário)
[]#Vertice 15(João)

    }

    start = 0
    target_filipa = 13
    target_mario = 14
    target_joao = 15

    path_filipa, route_filipa = dijkstra(start, target_filipa, graph)
    path_mario, route_mario = dijkstra(start, target_mario, graph)
    path_joao, route_joao = dijkstra(start, target_joao, graph)

    if path_filipa < path_joao and path_filipa < path_mario:
        print(f"O caminho até a Filipa é o menor, com duração de {path_filipa} minutos.")
        print(f"Caminho percorrido: {route_filipa}")
        print("O caminho começa no vértice User, vai a Fotografia e depois vai até a Filipa")
    elif path_joao < path_filipa and path_joao < path_mario:
        print(f" caminho até o João é o menor, com duração de {path_joao} minutos.")
        print(f"Caminho percorrido: {route_joao}")
    elif path_mario < path_filipa and path_mario < path_joao:
        print(f" caminho até o Mário é o menor, com duração de {path_mario} minutos.")
        print(f"Caminho percorrido: {route_mario}")

if __name__ == "__main__":
    main()
