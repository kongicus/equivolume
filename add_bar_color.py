import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def add_col_bar_color(stock_data, color, volume_min_excluded: float, volume_max_excluded: float):
    # Compute color mapping.
    norm = mcolors.Normalize(vmin=volume_min_excluded, vmax=volume_max_excluded)
    colormap = plt.colormaps.get_cmap(color)

    # Set the color for each bar.
    stock_data['color'] = [colormap(norm(vol)) for vol in stock_data['Volume']]
    return stock_data
