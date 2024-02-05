class PriorityQueue:
    def __init__(self):
        self.queue = {}

    def push(self, item, priority):
        if priority in self.queue:
            self.queue[priority].append(item)
        else:
            self.queue[priority] = [item]

    def pop(self):
        if not self.isEmpty():
            highest_priority = min(self.queue.keys())
            item = self.queue[highest_priority].pop(0)
            if not self.queue[highest_priority]:
                del self.queue[highest_priority]
            return item

    def isEmpty(self):
        return not bool(self.queue)

def AStar(graph, heuristic, startNode, goal):
    open_set = PriorityQueue()  
    open_set.push(startNode, 0)
    came_from = {}
    cost_so_far = {startNode: 0}

    while not open_set.isEmpty():
        current = open_set.pop()

        if current == goal:
            current = goal
            path = []

            while current != startNode:
                path.append(current)
                current = came_from[current]

            path.append(startNode)
            path.reverse()

            return path, cost_so_far[goal]

        for neighbor, cost_to_reach_neighbor in graph[current].items():
            new_cost = cost_so_far[current] + cost_to_reach_neighbor

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                open_set.push(neighbor, priority)
                came_from[neighbor] = current

    return None, 0  # No path found

graph = {
    'A': {'Z': 75, 'T': 118, 'S': 140},
    'B': {'G': 90, 'P': 101,'U':85,'F':211},
    'C': {'D': 120 ,'R': 146, 'P':138},
    'D': {'C': 120, 'M': 75},
    'E': {'H': 86},
    'F':{'B':211, 'S':99},
    'G':{'B':90},
    'H':{'E':86, 'U':98},
    'I':{'N':87, 'V':92},
    'L':{'T':111, 'M':70},
    'M':{'L':70,'D':75},
    'N':{'I':87},
    'O':{'Z':71, 'S':151},
    'P':{'R':97, "C":138, 'B':101},
    'R':{'P':97, "S":80, 'C':146},
    'S':{'O':151, 'A':140, 'F':99, 'R':80},
    'T':{'A':118, 'L':111},
    'U':{'B':85, 'V':142, 'H':98},
    'V':{'I':92, 'U':142},
    'Z':{'O':71, 'A':75},   
}
heuristic = {
    'A': 366,'B': 0,'C': 160,'D': 242,'E': 161,'F': 178,'G': 77,'H': 151,'I': 226,'L': 244,
    'M': 241,'N': 234,'O': 380,'P': 98,'R': 193,'S': 253,'T': 329,'U': 80,'V': 199,'Z': 374
}
start_node = 'A'
goal_node = 'B'
path,cost = AStar(graph, heuristic, start_node, goal_node)
print(path)  
print("Cost:", cost)