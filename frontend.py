import tkinter as tk
from tkinter import ttk
# if faut installer ceci
from ttkthemes import ThemedStyle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


from plot_it import speed_test

# from plot_it import speed_test
from analysis import signal_analysis
sa = signal_analysis()
button_list = []


root = tk.Tk()
root.geometry("400x400")
root.title("Mohamed Saifeddine et Khalil")


# Apply a modern theme to the application
style = ThemedStyle(root)
style.set_theme("yaru")

def refresh():
    for button in button_list:
        del button
    # Create a themed button
    for network in sa.list_wifi_names():
        button_list.append(ttk.Button(root, text=network+"  "+str("%.2f" % sa.one_signal_power_dbm(network)),command=speed_test(network).show_graph))
        button_list[-1].pack(side=tk.BOTTOM, padx=5)  # Align button to the left

    del button_list[0]
refresh_button = ttk.Button(root, text="Refresh", command = refresh)
refresh_button.pack(side=tk.TOP, padx=5)

refresh()

root.mainloop()
