from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from analysis import signal_analysis

sa = signal_analysis()


class speed_test:
    def __init__(self, signal_name):
        self.signal_name = signal_name
        self.x_data = []
        self.y_data = []
        self.figure = plt.figure()
        self.line, = plt.plot_date(self.x_data, self.y_data, '-')
        self.animation = FuncAnimation(self.figure, self.update, interval=200,cache_frame_data=False)

    def update(self, frame):
        print(self.signal_name)
        self.x_data.append(datetime.now())
        self.y_data.append(sa.one_signal_power_dbm(self.signal_name))
        self.line.set_data(self.x_data, self.y_data)
        self.figure.gca().relim()
        self.figure.gca().autoscale_view()
        return self.line,

    def show_graph(self):
        animation = self.animation
        
        print(self.animation)
        self.animation = FuncAnimation(self.figure, self.update, interval=200,cache_frame_data=False)
        print(self.animation)
        plt().show()


#ts = speed_test()
#ts.show_graph()
