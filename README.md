Run
```commandline
python gui_equivolume.py
```

# About entering the names of stocks, futures, and other trading instruments
Enter a code like "AAPL". If using the TDX data source, enter a code like "600036".

# 使用通达信tdx作为数据源的时候
数据源从"Yahoo"选择到"tdx"，只支持"1d"（日线）级别的绘图。
获取通达信数据使用的是[mootdx](https://github.com/mootdx/mootdx)库。
使用前请先打开通达信（默认使用的原生通达信，安装目录是`C:\new_tdx`，如果安装目录不一样的话，需要改成自己的目录。
