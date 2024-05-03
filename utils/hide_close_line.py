import matplotlib.pyplot as plt


def set_close_line(hide_close_line: bool, stock_data):
    # Add 'Close' price in every bar, can be hidden
    if not hide_close_line:
        return plt.hlines(stock_data['Close'],
                          xmin=stock_data['x_location'] - stock_data['Volume_coefficient'] / 2,
                          xmax=stock_data['x_location'] + stock_data['Volume_coefficient'] / 2,
                          colors='black')
    else:
        return None
