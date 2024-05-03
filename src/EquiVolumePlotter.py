import yfinance as yf
import matplotlib.pyplot as plt

from utils.add_col_coefficient import add_col_coefficient, get_min_max_of_volume
from utils.add_bar_color import add_col_bar_color
from utils.hide_edge_line import set_edge_line
from utils.hide_close_line import set_close_line
from utils.set_x_axis import set_x_axis_label
from utils.add_x_axis_location import add_x_axis_location
from utils.get_data_tdx import get_tdx_daily_data


class EquiVolumePlotter:
    """
    :param tickers: Name of the trading instrument, e.g., "AAPL".
    :param start_date: Start date for the chart, e.g., "2024-01-01".
    :param end_date: End date for the chart, e.g., "2024-12-31".
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

    def __init__(self, ticker: str, start_date: str, end_date: str, time_interval: str, color: str,
                 hide_close_line: bool, hide_edge_line: bool, data_src: str, tdx_dir: str):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.time_interval = time_interval
        self.color = color
        self.hide_close_line = hide_close_line
        self.hide_edge_line = hide_edge_line
        self.tdx_dir = tdx_dir
        self.stock_data = self.get_data(data_src)
        self.volume_min_excluded, self.volume_max_excluded = get_min_max_of_volume(self.stock_data)
        self.stock_data = self.impute_data()

    def get_data(self, data_src):
        if data_src == "Yahoo":
            stock_data = yf.download(tickers=self.ticker,
                                     start=self.start_date,
                                     end=self.end_date,
                                     interval=self.time_interval)
            return stock_data
        elif data_src == "tdx":
            self.time_interval = "1d"
            stock_data = get_tdx_daily_data(ticker=self.ticker, start=self.start_date, end=self.end_date,
                                            interval=self.time_interval, tdx_dir=self.tdx_dir)
            return stock_data

    def impute_data(self):
        self.stock_data = add_col_coefficient(self.stock_data, self.volume_min_excluded, self.volume_max_excluded)
        self.stock_data = add_col_bar_color(self.stock_data, self.color, self.volume_min_excluded,
                                            self.volume_max_excluded)
        self.stock_data = add_x_axis_location(self.stock_data)
        return self.stock_data

    def plot_equivolume_chart(self):
        # Figure instance
        fig = plt.figure(figsize=(20, 12))

        # ax instance, the subplot in the figure that located in nrows=1 ncols=1, and index=1
        ax = fig.add_subplot(1, 1, 1)

        # Set the border color of the bar, default is black, can be hidden
        bar_edge_color = set_edge_line(self.hide_edge_line)

        # Draw a bar chart, where the x-axis is the cumulative sum of standardized trading volume,
        # and the height is the difference between the 'High' and 'Low'
        ax.bar(x=self.stock_data['x_location'],
               height=self.stock_data['High'] - self.stock_data['Low'],
               bottom=self.stock_data['Low'],
               width=self.stock_data['Volume_coefficient'],
               color=self.stock_data['color'],
               edgecolor=bar_edge_color)

        set_close_line(self.hide_close_line, self.stock_data)

        # set x-axis
        set_x_axis_label(ax, self.stock_data, self.time_interval)

        # Adjust the font size of the y-axis tick labels
        ax.tick_params(axis='y', labelsize=15)

        # add the ticker name as the title in the center, and add the time interval in the right
        ax.set_ylabel('Price', fontsize=15)
        ax.set_title(f'{self.ticker}', fontsize=20)
        ax.set_title(f'Time Interval: {self.time_interval}', fontsize=15, loc='right')

        # show the equivolume chart
        plt.tight_layout()
        plt.show()
