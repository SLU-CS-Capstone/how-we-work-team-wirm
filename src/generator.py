from maze import Maze
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=12)
maze = Maze(20)
maze.generate_maze()
maze.print()
maze_text = maze.print()
pdf.multi_cell(0, 10, txt=maze_text)
pdf.output("maze.pdf")
print("Welcome to 2D maze")
