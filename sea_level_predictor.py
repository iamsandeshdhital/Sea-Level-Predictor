import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    data = pd.read_csv("epa-sea-level.csv")
    figure, axis = plt.subplots(figsize=(10, 6))

    axis.scatter(data["Year"], data["CSIRO Adjusted Sea Level"])

    full_fit = linregress(
        data["Year"], data["CSIRO Adjusted Sea Level"]
    )
    full_years = pd.Series(range(data["Year"].min(), 2051))
    axis.plot(
        full_years,
        full_fit.intercept + full_fit.slope * full_years,
        color="red",
    )

    recent_data = data[data["Year"] >= 2000]
    recent_fit = linregress(
        recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"]
    )
    recent_years = pd.Series(range(2000, 2051))
    axis.plot(
        recent_years,
        recent_fit.intercept + recent_fit.slope * recent_years,
        color="green",
    )

    axis.set_xlabel("Year")
    axis.set_ylabel("Sea Level (inches)")
    axis.set_title("Rise in Sea Level")
    figure.savefig("sea_level_plot.png")
    return axis
