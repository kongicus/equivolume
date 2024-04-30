import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import yfinance as yf


def plot_volume_color(ticker: str,
                      start_date: str,
                      end_date: str,
                      time_interval: str,
                      color: str,
                      hide_close_line: bool=False):
    stock_data = yf.download(tickers=ticker, start=start_date, end=end_date, interval=time_interval)

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

    # 画柱状图，x轴为系数化的成交量的累积和，高度为每条数据的High和Low之差
    plt.bar(stock_data['x_location'], stock_data['High'] - stock_data['Low'],
            bottom=stock_data['Low'], width=stock_data['Volume_coefficient'],
            color=stock_data['color'], edgecolor='black')

    # 添加收盘价的黑色横线
    if not hide_close_line:
        plt.hlines(stock_data['Close'], xmin=stock_data['x_location'] - stock_data['Volume_coefficient'] / 2,
                   xmax=stock_data['x_location'] + stock_data['Volume_coefficient'] / 2, colors='black')

    # plt.xticks(stock_data['x_location'])

    # 不显示x轴标签
    plt.xticks([])

    # 添加标题和标签
    plt.ylabel('Price')
    plt.title(ticker)

    # 显示图形
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    symbol = "QQQ"
    start = "2021-01-01"
    end = "2024-04-29"
    time_inter = '1mo'
    # '1d'：每日数据
    # '5d'：最近五个交易日的数据
    # '1wk'：每周数据
    # '1mo'：每月数据
    # '3mo'：每季度数据
    # '6mo'：半年数据
    # '1y'：每年数据
    # '2y'：两年数据
    # '5y'：五年数据
    # '10y'：十年数据
    # 此外，你还可以请求分钟级别的数据，例如：
    #
    # '1m'：每分钟数据
    # '5m'：每5分钟数据
    # '15m'：每15分钟数据
    # '30m'：每30分钟数据
    # '60m'：每60分钟（每小时）数据
    iro = "Reds"
    # 'Blues'
    # 'Greens'
    # 'Reds'
    # 'Oranges'
    # 'Purples'
    # 'YlOrBr'
    # 'YlOrRd'
    # 'OrRd'
    # 'PuRd'
    # 'BuPu'
    # 'GnBu'
    # 'PuBu'
    # 'YlGnBu'
    # 'PuBuGn'
    # 'BuGn'
    # 'YlGn'

    # x_lable_time_inter = "MS"
    # B：表示工作日（business day）。例如，B表示按工作日计算，BM表示按工作日的月末。
    # D：表示日历日（calendar day）。例如，D表示按日计算，BDS表示每个商业月的最后一个工作日。
    # W：表示周。例如，W表示每周，W-SUN表示每周的星期日。
    # M：表示月。例如，M表示每月，MS表示每月的第一天。
    # Q：表示季度。例如，Q表示每季度，QS表示每季度的第一个月的第一天。
    # A：表示年。例如，A表示每年，AS表示每年的第一天。

    plot_volume_color(ticker=symbol,
                      start_date=start,
                      end_date=end,
                      color=iro,
                      time_interval=time_inter)
