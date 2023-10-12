from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from analysis import signal_analysis

sa = signal_analysis()


class speed_test:
    def __init__(self):
        self.x_data = []
        self.y_data = []
        self.figure = plt.figure()
        self.line, = plt.plot_date(self.x_data, self.y_data, '-')

    def update(self, frame):
        self.x_data.append(datetime.now())
        self.y_data.append(sa.one_signal_power_dbm('Infinix SMART 5'))
        self.line.set_data(self.x_data, self.y_data)
        self.figure.gca().relim()
        self.figure.gca().autoscale_view()
        return self.line,

    def show_graph(self):
        animation = FuncAnimation(self.figure, self.update, interval=200)
        plt.show()


ts = speed_test()
ts.show_graph()
