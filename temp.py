import tkinter as tk
from tkinter import messagebox
from heapq import heappop, heappush

def heuristic(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))  # Chebyshev distance

def solve_warehouse(layout, start_item, end_item):
    # Parse the layout into a grid
    grid = [list(map(int, line.split())) for line in layout.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    # Find the start and end positions
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == start_item:
                start = (r, c)
            elif grid[r][c] == end_item:
                end = (r, c)
    
    if not start or not end:
        return None, "Invalid layout: Missing start or end item."
    
    # Directions for moving in the grid (right, down, left, up, and diagonals)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    # A* search to find the shortest path
    open_set = []
    heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    
    while open_set:
        _, current = heappop(open_set)
        
        if current == end:
            break
        
        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heappush(open_set, (f_score[neighbor], neighbor))
    
    # Reconstruct the path
    path = []
    step = end
    while step in came_from:
        path.append(step)
        step = came_from[step]
    path.append(start)
    path.reverse()
    
    if path[0] == start:
        for r, c in path:
            grid[r][c] = '*'
        return grid, "Path found."
    else:
        return None, "No path found."

def draw_warehouse(grid):
    if not grid:
        return ""
    
    rows, cols = len(grid), len(grid[0])
    border_top = "+" + "---+" * cols
    result = border_top + "\n"
    
    for row in grid:
        result += "| " + " | ".join(f"{cell:2}" for cell in row) + " |\n"
        result += border_top + "\n"
    
    return result

def display_result(grid, message):
    result_text.delete(1.0, tk.END)
    if grid:
        result_text.insert(tk.END, draw_warehouse(grid))
    result_text.insert(tk.END, message)

def find_path():
    try:
        start_item = int(start_entry.get())
        end_item = int(end_entry.get())
        grid, message = solve_warehouse(warehouse_layout, start_item, end_item)
        display_result(grid, message)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid integers for start and end items.")

# Example layout
warehouse_layout = """
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""

# Create the main window
root = tk.Tk()
root.title("Warehouse Pathfinding")

# Create input fields and labels
tk.Label(root, text="Enter the item you are coming from:").grid(row=0, column=0, padx=10, pady=5)
start_entry = tk.Entry(root)
start_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the item you want to get to:").grid(row=1, column=0, padx=10, pady=5)
end_entry = tk.Entry(root)
end_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a button to find the path
find_button = tk.Button(root, text="Find Path", command=find_path)
find_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a text widget to display the result
result_text = tk.Text(root, height=15, width=50)
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()

