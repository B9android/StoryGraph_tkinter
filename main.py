import os
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import pygraphviz as pgv


root_window = tk.Tk()
root_window.geometry('1800x1000')
root_window.title('StoryGraph')


def select_dir():
    folder_path = filedialog.askdirectory(mustexist=True, parent=root_window, initialdir=".")
    if folder_path:
        selected_dir.set(folder_path)
        list_files(folder_path)


def list_files(folder_path):
    for child in tree_view.get_children():
        tree_view.delete(child)

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            tree_view.insert("", "end", values=(filename,))


selected_dir = tk.StringVar(root_window)
select_dir_button = tk.Button(root_window, text="Select Markdown Directory", command=select_dir)
select_dir_button.pack()

tree_view = ttk.Treeview(root_window, columns=("Files",), show="headings", selectmode="browse")
tree_view.heading("Files", text="Files in Directory")
tree_view.pack()

root_window.mainloop()
