from collections import deque
import time

def bfs(maze, start, goal):
    """
    BFS algorithm to find shortest path in maze
    """
    start_time = time.time()
    
    rows = len(maze)
    cols = len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_expanded = 0
  
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        current, path = queue.popleft()
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
                
                visited.add(new_pos)
                queue.append((new_pos, path + [new_pos]))
    
    end_time = time.time()
    return {
        'path': [],
        'steps': 0,
        'nodes_explored': nodes_expanded,
        'time': end_time - start_time,
        'success': False
    }