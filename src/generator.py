from maze import Maze

mazeSize = input("What size would you like the maze to be?: ")

maze = Maze(mazeSize)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")