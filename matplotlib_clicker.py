import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_point_clicker import clicker
from mpl_interactions import zoom_factory, panhandler


def point_added_cb(position, clicker_class: str):
    x, y = position
    print(f"New point of class {clicker_class} added at {x=:.2f}, {y=:.2f}")


fig, ax = plt.subplots(constrained_layout=True)
image = mpimg.imread('static/stinkbug.png')
ax.imshow(image)

# add zooming and middle click to pan
zoom_factory(ax)
ph = panhandler(fig, button=2)

my_clicker = clicker(
    ax,
    ["Circle", "Cross", "Star"],
    markers=["o", "x", "*"]
)

my_clicker.on_point_added(point_added_cb)


