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

    # 找到除去最新一个数据的最小值
    volume_min_excluded = stock_data['Volume'][:-1].min()
    volume_max_excluded = stock_data['Volume'][:-1].max()

    # 系数
    coefficient = 100 / (volume_max_excluded - volume_min_excluded)
    stock_data['Volume_coefficient'] = stock_data['Volume'] * coefficient

    # x轴位置，每根柱子的位置设置为每根柱子宽度的一半，以使其靠左对齐
    stock_data['x_location'] = stock_data['Volume_coefficient'].cumsum() - stock_data['Volume_coefficient'] / 2

    # 计算颜色映射
    norm = mcolors.Normalize(vmin=volume_min_excluded, vmax=volume_max_excluded)
    colormap = plt.colormaps.get_cmap(color)

    # 设置每个柱子的颜色
    stock_data['color'] = [colormap(norm(vol)) for vol in stock_data['Volume']]

    fig, ax = plt.subplots()

    # 设置bar的边线颜色，默认黑色，可以指定隐藏
    if not hide_edge_line:
        bar_edge_color = 'black'
    else:
        bar_edge_color = None

    # 画柱状图，x轴为系数化的成交量的累积和，高度为每条数据的High和Low之差
    ax.bar(x=stock_data['x_location'], height=stock_data['High'] - stock_data['Low'],
           bottom=stock_data['Low'], width=stock_data['Volume_coefficient'],
           color=stock_data['color'], edgecolor=bar_edge_color)

    # 添加收盘价的黑色横线
    if not hide_close_line:
        plt.hlines(stock_data['Close'], xmin=stock_data['x_location'] - stock_data['Volume_coefficient'] / 2,
                   xmax=stock_data['x_location'] + stock_data['Volume_coefficient'] / 2, colors='black')

    # 不显示x轴标签
    ax.set_xticks([])

    # 添加标题和标签
    ax.set_ylabel('Price')
    ax.set_title(f'{ticker} time interval: {time_interval}')

    # 显示图形
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    symbol = "QQQ"
    start = "2024-04-24"
    end = "2024-05-01"
    time_inter = '5m'
    iro = "Reds"
    hide_close = True
    hide_bar_edge = False

    plot_equivolume(ticker=symbol,
                    start_date=start,
                    end_date=end,
                    color=iro,
                    time_interval=time_inter,
                    hide_close_line=hide_close,
                    hide_edge_line=hide_bar_edge)
