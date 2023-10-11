import tkinter as tk
from tkinter import ttk
# if faut installer ceci
from ttkthemes import ThemedStyle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# from plot_it import speed_test
from analysis import signal_analysis
sa = signal_analysis()

root = tk.Tk()
root.title("mohammed saif eddine et khalil")


# Apply a modern theme to the application
style = ThemedStyle(root)
style.set_theme("yaru")

# Create a themed button
for network in sa.list_wifi_names():
    button = ttk.Button(root, text=network)
    button.pack(side=tk.LEFT, padx=5)  # Align button to the left


root.mainloop()
