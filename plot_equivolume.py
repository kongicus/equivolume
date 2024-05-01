import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def plot_equivolume(ticker: str,
                    stock_data,
                    time_interval: str,
                    color: str,
                    hide_close_line: bool,
                    hide_edge_line: bool):
    """
    Plot an equivolume chart.

    :param ticker: Name of the trading instrument, e.g., "AAPL".
    :param stock_data: DateFrame from yahoo finance.
    :param time_interval: Time interval for the data, accepts intervals such as:
        "1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo".
        Intraday data cannot extend last 60 days. (default is '1d')
    :param color: Color scheme for the chart, accepts colors such as:
        'Blues', 'Greens', 'Reds', 'Oranges', 'Purples', 'YlOrBr', 'YlOrRd', 'OrRd',
        'PuRd', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'.
        (default is 'Reds')
    :param hide_close_line: Whether to hide the close line on the chart (default is False).
    :param hide_edge_line: Whether to hide the edge line on the chart (default is False).
    """

    # Find the minimum value excluding the latest data.
    volume_min_excluded = stock_data['Volume'][:-1].min()
    volume_max_excluded = stock_data['Volume'][:-1].max()

    # coefficient
    coefficient = 100 / (volume_max_excluded - volume_min_excluded)
    stock_data['Volume_coefficient'] = stock_data['Volume'] * coefficient

    # x-axis position, set the position of each bar to half of the width of each bar to align them to the left.
    stock_data['x_location'] = stock_data['Volume_coefficient'].cumsum() - stock_data['Volume_coefficient'] / 2

    # Compute color mapping.
    norm = mcolors.Normalize(vmin=volume_min_excluded, vmax=volume_max_excluded)
    colormap = plt.colormaps.get_cmap(color)

    # Set the color for each bar.
    stock_data['color'] = [colormap(norm(vol)) for vol in stock_data['Volume']]

    fig, ax = plt.subplots()

    # Set the border color of the bar, default is black, can be hidden
    if not hide_edge_line:
        bar_edge_color = 'black'
    else:
        bar_edge_color = None

    # Draw a bar chart, where the x-axis is the cumulative sum of standardized trading volume,
    # and the height is the difference between the 'High' and 'Low'
    ax.bar(x=stock_data['x_location'], height=stock_data['High'] - stock_data['Low'],
           bottom=stock_data['Low'], width=stock_data['Volume_coefficient'],
           color=stock_data['color'], edgecolor=bar_edge_color)

    # add 'Close' price in every bar, can be hidden
    if not hide_close_line:
        plt.hlines(stock_data['Close'], xmin=stock_data['x_location'] - stock_data['Volume_coefficient'] / 2,
                   xmax=stock_data['x_location'] + stock_data['Volume_coefficient'] / 2, colors='black')

    # set x-axis
    if time_interval in ["1d", "1wk", "1mo", "3mo"]:
        # show the label under the x-axis, show the first day of every month
        month_starts = stock_data[stock_data.index.is_month_start]['x_location']
        ax.set_xticks(month_starts)
        ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in stock_data.index[stock_data.index.is_month_start]], rotation=45)
    else:
        # Display 5 time labels evenly on the x-axis for reference.
        num_ticks = 5
        num_data_points = len(stock_data)
        interval_size = num_data_points // num_ticks

        # Selecting data points at even intervals
        selected_data_points = stock_data.iloc[::interval_size]['x_location']

        ax.set_xticks(selected_data_points)
        ax.set_xticklabels([date.strftime('%Y-%m-%d %H:%M') for date in stock_data.index[::interval_size]], rotation=45)

    # add the ticker name as the title in the center, and add the time interval in the right
    ax.set_ylabel('Price')
    ax.set_title(f'{ticker}', fontsize=16)
    ax.set_title(f'Time Interval: {time_interval}', fontsize=12, loc='right')

    # show the equivolume chart
    plt.tight_layout()
    plt.show()
