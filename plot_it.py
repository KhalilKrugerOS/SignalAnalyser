from datetime import datetime
import matplotlib.pyplot as plt
from random import randrange
from matplotlib.animation import FuncAnimation
import numpy as np
from analysis import signal_analysis
# from analysis import signal_analysis


class test_speed:
    def __init__(self, x_data, y_data):
        x_data = self.x_data
        self.y_data = y_data
        x_data = []
        y_data = []
        figure = plt.figure()
        line, = plt.plot_date(x_data, y_data, '-')

    def update(self, figure):
        self.x_data.append(datetime.now())
        self.y_data.append(randrange(0, 100))
        self.line.set_data(self.x_data, self.y_data)
        figure.gca().relim()
        figure.gca().autoscale_view()
        return line,

    def show_graph(self):
        animation = FuncAnimation(figure, update, interval=200)
        plt.show()
