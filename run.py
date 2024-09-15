from pathfinding_visualiser.main import visualiser

import tkinter as tk
from tkinter.ttk import Style


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("750x750")
    root.resizable(True, True)
    root.title("Pathfinding Visualiser")
    root.config(bg="#17181c")


    lbl = tk.Label(root, text="Graph Search Visualiser", 
                   font = ("Arial",25,"bold"), padx=10, pady=10, 
                   width=30, background="#17181c", foreground="white")
    lbl.pack()

    text="""
    Below you can select which graph search algorithm to use.
    Breadth First Search will find the shortest path between the start and
    end points. 
    Depth First Search will find a path but does not guarantee 
    the shortest.

    You can generate a random maze by selecting checkbox, or you can draw
    the barriers yourself using the controls listed below.

    Controls:
    - left mouse click: select start and end point, draw barriers on grid.
    - right mouse click: reset and individual grid point.
    - c: clear the grid
    - r: reset the grid to state before search algorithm ran.
    - Enter: Start search algorithm (start and end must be picked)
    """
    text_widget = tk.Text(root, height=20, width=70, bg="#17181c", fg="white", 
                   font = ("Arial",10,"bold"), highlightbackground="#17181c",
                   bd=0)
    text_widget.pack(pady=5)
    text_widget.insert(tk.END, text)
    text_widget.config(state=tk.DISABLED)

    
    radio_var = tk.IntVar()
    radio_var.set(1)
    tk.Radiobutton(root, text="Breadth First Search", variable=radio_var, 
                   value=1, selectcolor="#17181c", bg="#17181c", fg="white", 
                   highlightbackground="#17181c",
                   font=("Arial",10,"bold")).pack(anchor=tk.CENTER, pady=10)
    
    tk.Radiobutton(root, text="Depth First Search", variable=radio_var, 
                   value=2, selectcolor="#17181c", bg="#17181c", fg="white", 
                   highlightbackground="#17181c", 
                   font = ("Arial",10,"bold")).pack(anchor=tk.CENTER, pady=10)
    
    check_var = tk.IntVar()
    check_var.set(0)

    tk.Checkbutton(root, text="Generate Maze", variable=check_var, onvalue=1, 
                   offvalue=0, selectcolor="#17181c", bg="#17181c", fg="white",
                   highlightbackground="#17181c", 
                   font = ("Arial",10,"bold"), bd=0).pack(pady=10)

    btn = tk.Button(root, text="Run Visualiser", width=20, height = 1, 
                    background="#17181c", foreground="white",
                    font = ("Arial",15,"bold"), highlightbackground="#17181c",
                    command=lambda: visualiser(radio_var.get(), bool(check_var.get())))
    btn.pack(pady=10)

    root.mainloop()


