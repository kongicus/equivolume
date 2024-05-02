def add_col_coefficient(stock_data, volume_min, volume_max):
    coefficient = 100 / (volume_max - volume_min)
    stock_data['Volume_coefficient'] = stock_data['Volume'] * coefficient
    return stock_data


def get_min_max_of_volume(stock_data):
    # Find the minimum value excluding the latest data.
    volume_min_excluded = stock_data['Volume'][:-1].min()
    volume_max_excluded = stock_data['Volume'][:-1].max()
    return volume_min_excluded, volume_max_excluded
