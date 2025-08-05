import streamlit as st
import matplotlib.pyplot as plt

from bfs import bfs
from dfs import dfs
from astar import astar

from mazeconf import MAZES
from visualization import draw_maze

def main():
    st.title("🔍 Maze Pathfinding Project")
    st.write("Compare different search algorithms: BFS, DFS, and A*")
    
    st.sidebar.header("Settings")
    
    problem = st.sidebar.selectbox("Choose a problem:", list(MAZES.keys()))
    
    algorithm = st.sidebar.radio(
        "Choose algorithm:",
        ["BFS", "DFS", "A*"]
    )
    
    maze_data = MAZES[problem]
    maze = maze_data["maze"]
    start = maze_data["start"]
    goal = maze_data["goal"]
    
    st.sidebar.write(f"**Start:** {start}")
    st.sidebar.write(f"**Goal:** {goal}")
    st.sidebar.write(f"**Size:** {len(maze)}x{len(maze[0])}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Maze Layout")
        
        fig = draw_maze(maze, start, goal)
        st.pyplot(fig)
        plt.close()
    
    with col2:
        st.subheader("Controls")
        
        if st.button("🚀 Find Path", type="primary"):
            
            with st.spinner("Searching..."):
                if algorithm == "BFS":
                    result = bfs(maze, start, goal)
                elif algorithm == "DFS":
                    result = dfs(maze, start, goal)
                else: 
                    result = astar(maze, start, goal)
            
            st.session_state['result'] = result
            st.session_state['current_maze'] = maze
            st.session_state['current_start'] = start
            st.session_state['current_goal'] = goal
            st.session_state['current_algorithm'] = algorithm
    
    if 'result' in st.session_state:
        result = st.session_state['result']
        
        st.divider()
        
        if result['success']:
            st.success(f"✅ Path found using {st.session_state['current_algorithm']}!")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("Solution")
                fig = draw_maze(st.session_state['current_maze'], 
                              st.session_state['current_start'], 
                              st.session_state['current_goal'], 
                              result['path'])
                st.pyplot(fig)
                plt.close()
            
            with col2:
                st.subheader("Results")
                st.metric("Steps", result['steps'])
                st.metric("Nodes Explored", result['nodes_explored'])
                st.metric("Time (seconds)", f"{result['time']:.4f}")
                
                st.subheader("Path")
                path_text = ""
                for i, pos in enumerate(result['path']):
                    if i > 0:
                        path_text += " → "
                    path_text += f"{pos}"
                st.text_area("Route:", path_text, height=100)
        
        else:
            st.error(f"❌ No path found using {st.session_state['current_algorithm']}!")
            st.metric("Nodes Explored", result['nodes_explored'])
            st.metric("Time (seconds)", f"{result['time']:.4f}")
    
    st.divider()
    st.subheader("Legend")
    st.write("🟩 **Green** = Start position")
    st.write("🟥 **Red** = Goal position")
    st.write("🟦 **Blue** = Walls")
    st.write("⬜ **White** = Free path")
    st.write("🟨 **Yellow** = Solution path")
    
    with st.expander("About the Algorithms"):
        st.markdown("""
        **BFS (Breadth-First Search):**
        - Explores level by level
        - Always finds shortest path
        - Uses more memory
        
        **DFS (Depth-First Search):**
        - Goes deep first, then backtracks
        - Uses less memory
        - May not find shortest path
        
        **A* (A-Star):**
        - Uses heuristic to guide search
        - Usually fastest and optimal
        - Good balance of time and space
        """)

if __name__ == "__main__":
    main()