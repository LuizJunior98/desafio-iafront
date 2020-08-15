import pandas as pd
import numpy as np
from bokeh.plotting import figure


def plot(dataframe: pd.DataFrame, x_axis, y_axis, title="", graph_type="hist"):
    colors = [set_color(_) for _ in [0, 1, 2, 3, 4]]
    p = figure(title=title)

    if graph_type.lower().strip() == "scatter":
        p.scatter(dataframe[x_axis].tolist(), dataframe[y_axis].tolist(), fill_color=colors)
    else:
        hist, edges = np.histogram(dataframe[y_axis].tolist(), bins=dataframe[y_axis].unique().size)
        p = figure()
        p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color=colors)

    return p


def _unique(original):
    return list(set(original))


def set_color(color):
    COLORS = ["green", "blue", "red", "orange", "purple"]

    index = color % len(COLORS)

    return COLORS[index]
