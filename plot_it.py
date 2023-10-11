from datetime import datetime
import matplotlib.pyplot as plt
from random import randrange
from matplotlib.animation import FuncAnimation
import numpy as np
from analysis import signal_analysis
# from analysis import signal_analysis


class test_speed:
    def __init__(self):
        
        self.x_data = []
        self.y_data = []
        self.figure = plt.figure()
        self.line, = plt.plot_date(self.x_data, self.y_data, '-')

    def update(self, frame):
        signal_analysis1 = signal_analysis()
        self.x_data.append(datetime.now())
        self.y_data.append(signal_analysis1.wifi_signal_power_analyser())
        self.line.set_data(self.x_data, self.y_data)
        self.figure.gca().relim()
        self.figure.gca().autoscale_view()
        return self.line,

    def show_graph(self):
        animation = FuncAnimation(self.figure, self.update, interval=200)
        plt.show()
