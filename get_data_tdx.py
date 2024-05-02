import pandas as pd
from mootdx.reader import Reader


def get_tdx_daily_raw_data(ticker: str, interval: str, tdx_dir: str):
    reader = Reader.factory(market='std', tdxdir=r'{}'.format(tdx_dir))
    if interval == "1d":
        return reader.daily(symbol=ticker)
    else:
        raise ValueError("Please select a time interval of 1d.")


def select_data(tdx_data, start_time: str, end_time: str):
    selected_data = tdx_data.loc[start_time:end_time]
    return selected_data.copy()


def organize_df_column_names(tdx_data):
    tdx_data.rename(columns={'volume': 'Volume'}, inplace=True)
    tdx_data.rename(columns={'open': 'Open'}, inplace=True)
    tdx_data.rename(columns={'high': 'High'}, inplace=True)
    tdx_data.rename(columns={'low': 'Low'}, inplace=True)
    tdx_data.rename(columns={'close': 'Close'}, inplace=True)
    return tdx_data


def get_tdx_daily_data(ticker: str, start: str, end: str, interval: str, tdx_dir: str):
    raw_data = get_tdx_daily_raw_data(ticker, interval, tdx_dir)
    selected_stock_data = select_data(tdx_data=raw_data, start_time=start, end_time=end)
    modify_tdx_data = organize_df_column_names(selected_stock_data)
    return modify_tdx_data
