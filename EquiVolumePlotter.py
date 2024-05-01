import yfinance as yf
from plot_equivolume import plot_equivolume


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
    def __init__(self, ticker: str, start_date: str, end_date: str, time_interval: str = '1d', color: str = 'Reds', hide_close_line: bool = False, hide_edge_line: bool = False):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.time_interval = time_interval
        self.color = color
        self.hide_close_line = hide_close_line
        self.hide_edge_line = hide_edge_line

    def get_data(self):
        stock_data = yf.download(tickers=self.ticker,
                                 start=self.start_date,
                                 end=self.end_date,
                                 interval=self.time_interval)
        return stock_data

    def plot(self):
        stock_data = self.get_data()
        plot_equivolume(self.ticker, stock_data, self.time_interval, self.color, self.hide_close_line, self.hide_edge_line)


if __name__ == "__main__":
    equi_volume_plotter = EquiVolumePlotter(ticker="AAPL", start_date="2024-01-01", end_date="2024-05-01")
    equi_volume_plotter.plot()
