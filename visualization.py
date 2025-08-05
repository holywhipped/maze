import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_maze(maze, start, goal, path=None):
    """
    Draw the maze with start, goal, and optional path
    """
    rows = len(maze)
    cols = len(maze[0])
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1: 
                rect = patches.Rectangle((j, rows-1-i), 1, 1, 
                                       facecolor='blue', edgecolor='black')
            else: 
                rect = patches.Rectangle((j, rows-1-i), 1, 1, 
                                       facecolor='white', edgecolor='gray')
            ax.add_patch(rect)
    
    start_rect = patches.Rectangle((start[1], rows-1-start[0]), 1, 1, 
                                 facecolor='green', edgecolor='black', linewidth=2)
    ax.add_patch(start_rect)
    
    goal_rect = patches.Rectangle((goal[1], rows-1-goal[0]), 1, 1, 
                                facecolor='red', edgecolor='black', linewidth=2)
    ax.add_patch(goal_rect)
    
    if path:
        for pos in path[1:-1]: 
            path_rect = patches.Rectangle((pos[1], rows-1-pos[0]), 1, 1, 
                                        facecolor='yellow', alpha=0.7, edgecolor='black')
            ax.add_patch(path_rect)
    
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.set_xticks(range(cols+1))
    ax.set_yticks(range(rows+1))
    ax.grid(True)
    
    return fig