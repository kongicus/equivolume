def set_x_axis_label(ax, stock_data, time_interval):
    # set x-axis
    if time_interval in ["1d", "1wk", "1mo", "3mo"]:
        # show the label under the x-axis, show the first day of every month
        month_starts = stock_data[stock_data.index.is_month_start]['x_location']
        ax.set_xticks(month_starts)
        ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in stock_data.index[stock_data.index.is_month_start]],
                           rotation=45)
    else:
        # Display 5 time labels evenly on the x-axis for reference.
        num_ticks = 5
        num_data_points = len(stock_data)
        interval_size = num_data_points // num_ticks

        # Selecting data points at even intervals
        selected_data_points = stock_data.iloc[::interval_size]['x_location']

        ax.set_xticks(selected_data_points)
        ax.set_xticklabels([date.strftime('%Y-%m-%d\n%H:%M') for date in stock_data.index[::interval_size]],
                           rotation=45, fontsize=13)
