import matplotlib

matplotlib.use("Agg")

from sea_level_predictor import draw_plot


if __name__ == "__main__":
    draw_plot()
    print("Created sea_level_plot.png")
