from pathfinding_visualiser.main import visualiser

import tkinter as tk
from tkinter.ttk import Style


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(True, True)
    root.title("Pathfinding Visualiser")
    root.config(bg="#17181c")


    lbl = tk.Label(root, text="Graph Search Visualiser", 
                   font = ("Arial",25,"bold"), padx=10, pady=10, 
                   width=20, background="#17181c", foreground="white")
    lbl.pack()
    
    radio_var = tk.IntVar()
    radio_var.set(1)
    tk.Radiobutton(root, text="Breadth First Search", variable=radio_var, value=1, 
                   selectcolor="#17181c", bg="#17181c", fg="white", 
                   pady=5, font = ("Arial",10,"bold")).pack(anchor=tk.CENTER)
    tk.Radiobutton(root, text="Depth First Search", variable=radio_var, value=2,
                    selectcolor="#17181c", bg="#17181c", fg="white", 
                    pady=5, font = ("Arial",10,"bold")).pack(anchor=tk.CENTER)
    
    check_var = tk.IntVar()
    check_var.set(0)

    tk.Checkbutton(root, text="Generate Maze", variable=check_var, onvalue=1, 
                   offvalue=0, selectcolor="#17181c", bg="#17181c", fg="white", 
                    pady=5, font = ("Arial",10,"bold")).pack()

    btn = tk.Button(root, text="Run Visualiser", width=20, height = 1, 
                    background="#17181c", foreground="white",
                    font = ("Arial",15,"bold"),
                    command= lambda: visualiser(radio_var.get(), bool(check_var.get())))
    btn.pack()

    root.mainloop()


