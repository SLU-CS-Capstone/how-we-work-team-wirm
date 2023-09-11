from maze import Maze
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
maze = Maze(20)
maze.generate_maze()
maze.print()
pdf.cell(200, 10, txt=maze.print, ln=True)
pdf.output("example.pdf")
print("Welcome to 2D maze")
