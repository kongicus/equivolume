import customtkinter
from tkcalendar import DateEntry
import EquiVolumePlotter as evp


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EquiVolume")
        self.geometry("900x400")

        # Set the weight of each column to 1 so that they are evenly distributed horizontally.
        for i in range(6):
            self.grid_columnconfigure(i, weight=1)

        # input stock name
        self.ticker_name = customtkinter.CTkTextbox(self,
                                                    width=80,
                                                    height=10)
        self.ticker_name.insert(index="0.0",
                                text="AAPL")
        self.ticker_name.grid(row=0,
                              column=0,
                              padx=20,
                              pady=(20, 20),
                              sticky="ew")

        # Date picker for start date
        self.start_date_label = customtkinter.CTkLabel(self,
                                                       text="Start Date:",
                                                       font=("Arial", 16))
        self.start_date_label.grid(row=1,
                                   column=0,
                                   padx=20,
                                   pady=(0, 20),
                                   sticky="w")
        self.start_date_entry = DateEntry(self,
                                          width=10,
                                          date_pattern="yyyy-mm-dd",
                                          font=("Arial", 16))
        self.start_date_entry.grid(row=1,
                                   column=1,
                                   padx=20,
                                   pady=(0, 20),
                                   sticky="ew")

        # Date picker for end date
        self.end_date_label = customtkinter.CTkLabel(self,
                                                     text="End Date:",
                                                     font=("Arial", 16))
        self.end_date_label.grid(row=1,
                                 column=2,
                                 padx=20,
                                 pady=(0, 20),
                                 sticky="w")
        self.end_date_entry = DateEntry(self,
                                        width=10,
                                        date_pattern="yyyy-mm-dd",
                                        font=("Arial", 16))
        self.end_date_entry.grid(row=1,
                                 column=3,
                                 padx=20,
                                 pady=(0, 20),
                                 sticky="ew")

        # choose time interval
        self.time_interval_var = customtkinter.StringVar(value="1d")
        self.time_interval = customtkinter.CTkComboBox(self,
                                                       values=["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h",
                                                                     "1d", "1wk", "1mo", "3mo"],
                                                       width=70,
                                                       variable=self.time_interval_var)
        self.time_interval.grid(row=0,
                                column=1,
                                padx=20,
                                pady=(20, 20),
                                sticky="ew")

        # choose bar color
        self.bar_color_var = customtkinter.StringVar(value="Reds")
        self.bar_color = customtkinter.CTkComboBox(self,
                                                   values=['Blues', 'Greens', 'Reds', 'Oranges', 'Purples',
                                                           'YlOrBr', 'YlOrRd', 'OrRd',
                                                           'PuRd', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn',
                                                           'BuGn', 'YlGn'],
                                                   width=90,
                                                   variable=self.bar_color_var)
        self.bar_color.grid(row=0,
                            column=2,
                            padx=20,
                            pady=(20, 20),
                            sticky="ew")

        # hide_close_line
        self.hide_close_line_var = customtkinter.BooleanVar(value=False)
        self.hide_close_line = customtkinter.CTkCheckBox(self,
                                                         text="hide close line",
                                                         variable=self.hide_close_line_var)
        self.hide_close_line.grid(row=0,
                                  column=3,
                                  padx=20,
                                  pady=(20, 20),
                                  sticky="ew")

        # hide_edge_line
        self.hide_edge_line_var = customtkinter.BooleanVar(value=False)
        self.hide_edge_line = customtkinter.CTkCheckBox(self,
                                                        text="hide edge line",
                                                        variable=self.hide_edge_line_var)
        self.hide_edge_line.grid(row=0,
                                 column=4,
                                 padx=20,
                                 pady=(20, 20),
                                 sticky="ew")

        # plot button
        self.button = customtkinter.CTkButton(self,
                                              text="PLOT",
                                              command=self.plot_button)
        self.button.grid(row=0,
                         column=5,
                         padx=20,
                         pady=(20, 20),
                         sticky="ew")

    def plot_button(self):
        equi_volume_plotter = evp.EquiVolumePlotter(ticker=self.ticker_name.get("0.0", "end"),
                                                    start_date=self.start_date_entry.get(),
                                                    end_date=self.end_date_entry.get(),
                                                    time_interval=self.time_interval_var.get(),
                                                    color=self.bar_color_var.get(),
                                                    hide_close_line=self.hide_close_line_var.get(),
                                                    hide_edge_line=self.hide_edge_line_var.get())
        equi_volume_plotter.plot_equivolume_chart()


app = App()
app.mainloop()
