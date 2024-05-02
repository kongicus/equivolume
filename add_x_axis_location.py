def add_x_axis_location(stock_data):
    # x-axis position, set the position of each bar to half of the width of each bar to align them to the left.
    stock_data['x_location'] = stock_data['Volume_coefficient'].cumsum() - stock_data['Volume_coefficient'] / 2
    return stock_data
