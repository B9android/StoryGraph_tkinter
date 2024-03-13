import os
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import pygraphviz as pgv
import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root_window = tk.Tk()
root_window.geometry('1800x1000')
root_window.title('StoryGraph')

G = nx.DiGraph()


# G = pgv.AGraph(directed=True)
# G.layout(prog="dot")


def select_dir():
    folder_path = filedialog.askdirectory(mustexist=True, parent=root_window, initialdir=".")
    if folder_path:
        make_graph(folder_path)
        list_files(folder_path)


def list_files(folder_path):
    for child in tree_view.get_children():
        tree_view.delete(child)

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            tree_view.insert("", "end", values=(filename,))


def get_filenames(folder_path):
    filelist = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            filelist.append(filename)
    return filelist


def make_graph(selected_dir):
    print(selected_dir)
    nodelist = get_filenames(selected_dir)
    G.add_nodes_from(nodelist)
    plot(G)


def plot(G):
    fig = plt.figure()
    nx.draw(G, pos=graphviz_layout(G, prog="dot"))
    canvas = FigureCanvasTkAgg(fig, master=root_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, root_window)
    toolbar.update()
    canvas.get_tk_widget().pack()


select_dir_button = tk.Button(root_window, text="Select Markdown Directory", command=select_dir)
select_dir_button.pack()

tree_view = ttk.Treeview(root_window, columns=("Files",), show="headings", selectmode="browse")
tree_view.heading("Files", text="Files in Directory")
tree_view.pack()

root_window.mainloop()
