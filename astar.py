import time
import heapq

def manhattan_distance(pos1, pos2):
    """
    Calculate Manhattan distance between two positions
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def astar(maze, start, goal):
    """
    A* algorithm to find optimal path in maze
    """
    start_time = time.time()
    
    rows = len(maze)
    cols = len(maze[0])
    heap = [(0, start, [start], 0)]  
    visited = set()
    nodes_expanded = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while heap:
        f_cost, current, path, g_cost = heapq.heappop(heap)
        
        if current in visited:
            continue
            
        visited.add(current)
        nodes_expanded += 1
        
        if current == goal:
            end_time = time.time()
            return {
                'path': path,
                'steps': len(path) - 1,
                'nodes_explored': nodes_expanded,
                'time': end_time - start_time,
                'success': True
            }
        
        for dx, dy in directions:
            new_x = current[0] + dx
            new_y = current[1] + dy
            new_pos = (new_x, new_y)
            
            if (0 <= new_x < rows and 
                0 <= new_y < cols and 
                maze[new_x][new_y] == 0 and 
                new_pos not in visited):
                
                new_g_cost = g_cost + 1
                h_cost = manhattan_distance(new_pos, goal)
                new_f_cost = new_g_cost + h_cost
                new_path = path + [new_pos]
                
                heapq.heappush(heap, (new_f_cost, new_pos, new_path, new_g_cost))
    

    end_time = time.time()
    return {
        'path': [],
        'steps': 0,
        'nodes_explored': nodes_expanded,
        'time': end_time - start_time,
        'success': False
    }