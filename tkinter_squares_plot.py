import tkinter as tk
from tkinter import Tk, Button
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

# Sets colormap: 0 - red; 1 - green; 2 - black; 3 - yellow; 4 - blue;
CUSTOM_CMAP = mpl.colors.ListedColormap(['red', 'green', 'black', 'yellow', 'blue'])


class GraphFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.shift = 0

        # Draw button
        draw_button = Button(self, text="Re-calculate", command=self.draw_plot)

        # Figure and tk_canvas
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        # Toolbar
        toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        # Allows key to control the toolbar
        self.canvas.mpl_connect("key_press_event", key_press_handler)

        # Use grid to place elements
        draw_button.grid(row=0, column=0, padx=(10, 5))
        self.canvas.get_tk_widget().grid(row=0, column=1, padx=5, pady=5)
        toolbar.grid(row=1, column=1)

        # Draw the plot
        self.draw_plot()

    def draw_plot(self):
        # Random n by n matrix of numbers 0 to 4 (inclusive)
        n = 20

        random_data = np.random.randint(0, 5, size=(n, n))
        self.ax.clear()
        self.ax.matshow(random_data, cmap=CUSTOM_CMAP)
        self.ax.set_title(f'Random Grid')
        # Set grid positions
        self.ax.xaxis.set_ticks(np.arange(-0.5, n + 0.5, 1))
        self.ax.yaxis.set_ticks(np.arange(-0.5, n + 0.5, 1))
        # Turn off the tick labels
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        # Set the grid lines
        self.ax.grid(True, color="black", linewidth="2", linestyle="-")
        # update tk_canvas
        self.canvas.draw()

        # Cause the function to be redrawn after 0.2 seconds
        # self.after(200, self.draw_plot)


# plt.style.use('ggplot')
# GUI
root = Tk()
root.title("Sample Sine Wave Graph in Tkinter")
graph_page = GraphFrame()
graph_page.pack()

root.mainloop()
