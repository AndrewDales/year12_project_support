# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_point_clicker import clicker
from mpl_interactions import zoom_factory, panhandler


# Callback function - to be run when a point is added by the clicker
def point_added_cb(position, clicker_class: str):
    x, y = position
    print(f"New point of class '{clicker_class}' added at {x=:.2f}, {y=:.2f}")


# Creates a figure and axis in matplotlib
fig, ax = plt.subplots(constrained_layout=True)
# Reads the image file stored in the static sub-folder
image = mpimg.imread('static/stinkbug.png')
# Shows the image on the axis above
ax.imshow(image)
# Adds grid-lines to the axis
ax.grid()

# add zooming with mouse and middle click to pan
zoom_factory(ax)
ph = panhandler(fig, button=2)

# Creates the clicker object with three different types of clicker
my_clicker = clicker(
    ax,
    ["Circle", "Cross", "Star"],
    markers=["o", "x", "*"]
)

# Attaches the callback function that will be activated when the image is clicked.
my_clicker.on_point_added(point_added_cb)
