import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

playera = tk.StringVar()
playerb = tk.StringVar()
p1 = tk.StringVar()
p2 = tk.StringVar()


player1_name = tk.Entry(root, textvariable=p1, bd=5)
