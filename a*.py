import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g 
        self.h = h  
        self.f = g + h  

    def __lt__(self, other):  
        return self.f < other.f

def astar_search(graph, heuristics, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.name == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1]  # reverse path

        closed_set.add(current.name)

        for neighbor, cost in graph[current.name].items():
            if neighbor in closed_set:
                continue

            g = current.g + cost
            h = heuristics[neighbor]
            neighbor_node = Node(neighbor, current, g, h)
            if any(open_node.name == neighbor and open_node.f <= neighbor_node.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None
graph = {
    'HOME': {'BANK': 1, 'GARDEN': 3},
    'BANK': {'HOME': 1, 'SCHOOL': 3, 'RAILWAY': 1},
    'GARDEN': {'HOME': 3, 'POLICE STATION': 5},
    'SCHOOL': {'BANK': 3, 'OFFICE': 2},
    'RAILWAY': {'BANK': 1, 'OFFICE': 1},
    'POLICE STATION': {'GARDEN': 5, 'OFFICE': 2},
    'OFFICE': {'SCHOOL': 2, 'RAILWAY': 1, 'POLICE STATION': 2}
}
heuristics = {
    'HOME': 120,
    'BANK': 80,
    'GARDEN': 100,
    'SCHOOL': 70,
    'RAILWAY': 20,
    'POLICE STATION': 26,
    'OFFICE': 110
}
print("Enter Goal From the list \n HOME,BANK,GARDEN,SCHOOL,RAILWAY,POLICE STATION,OFFICE")
goal=str(input("Enter Path You Want yo find >> ")).upper()
start, goal = 'HOME', (f"{goal}")
path = astar_search(graph, heuristics, start, goal)
print(f"Shortest path from {start} to {goal}: {path}")







