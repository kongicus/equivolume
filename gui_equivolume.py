import customtkinter
from tkcalendar import DateEntry
from tkinter import filedialog

import EquiVolumePlotter as evp


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EquiVolume")
        self.geometry("700x500")

        # Set the weight of each column to 1 so that they are evenly distributed horizontally.
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

        # input stock name
        self.ticker_name = customtkinter.CTkTextbox(self,
                                                    width=35,
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
                                                       text="Start Date:")
        self.start_date_label.grid(row=1,
                                   column=0,
                                   padx=(20, 20),
                                   pady=(20, 20),
                                   sticky="e")
        self.start_date_entry = DateEntry(self,
                                          width=10,
                                          date_pattern="yyyy-mm-dd",
                                          font=("Arial", 16))
        self.start_date_entry.grid(row=1,
                                   column=1,
                                   padx=(20, 20),
                                   pady=(20, 20),
                                   sticky="w")

        # Date picker for end date
        self.end_date_label = customtkinter.CTkLabel(self,
                                                     text="End Date:")
        self.end_date_label.grid(row=1,
                                 column=2,
                                 padx=(20, 20),
                                 pady=(20, 20),
                                 sticky="e")
        self.end_date_entry = DateEntry(self,
                                        width=10,
                                        date_pattern="yyyy-mm-dd",
                                        font=("Arial", 16))
        self.end_date_entry.grid(row=1,
                                 column=3,
                                 padx=(20, 20),
                                 pady=(20, 20),
                                 sticky="w")

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
                                sticky="w")

        # choose bar color
        self.bar_color_var = customtkinter.StringVar(value="Reds")
        self.bar_color = customtkinter.CTkComboBox(self,
                                                   values=['Blues', 'Greens', 'Reds', 'Oranges', 'Purples',
                                                           'YlOrBr', 'YlOrRd', 'OrRd',
                                                           'PuRd', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn',
                                                           'BuGn', 'YlGn'],
                                                   width=70,
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
        self.hide_close_line.grid(row=2,
                                  column=0,
                                  padx=20,
                                  pady=(20, 20),
                                  sticky="ew")

        # hide_edge_line
        self.hide_edge_line_var = customtkinter.BooleanVar(value=False)
        self.hide_edge_line = customtkinter.CTkCheckBox(self,
                                                        text="hide edge line",
                                                        variable=self.hide_edge_line_var)
        self.hide_edge_line.grid(row=2,
                                 column=1,
                                 padx=20,
                                 pady=(20, 20),
                                 sticky="ew")

        # choose data_source
        self.data_source_var = customtkinter.StringVar(value="Yahoo")
        self.data_source = customtkinter.CTkComboBox(self,
                                                     values=['Yahoo', 'moomoo', 'tdx'],
                                                     width=90,
                                                     variable=self.data_source_var)
        self.data_source.grid(row=3,
                              column=0,
                              padx=20,
                              pady=(20, 20),
                              sticky="ew")

        # tdx dir input box
        self.tdx_dir_text = customtkinter.CTkLabel(self,
                                                   text="if use tdx, confirm the installation directory of tdx:",
                                                   font=("Arial", 16))
        self.tdx_dir_text.grid(row=4,
                               column=0,
                               columnspan=3,
                               padx=(20, 20),
                               pady=(20, 20),
                               sticky="w")
        self.tdx_dir_text_box = customtkinter.CTkTextbox(self,
                                                         width=35,
                                                         height=10)
        self.tdx_dir_text_box.insert(index="0.0",
                                     text="C:/new_tdx")
        self.tdx_dir_text_box.grid(row=5,
                                   column=0,
                                   padx=20,
                                   pady=(20, 20),
                                   sticky="ew")

        # plot button
        self.button = customtkinter.CTkButton(self,
                                              text="PLOT",
                                              command=self.plot_button)
        self.button.grid(row=6,
                         column=1,
                         columnspan=2,
                         pady=(20, 20),
                         sticky="ew")

    def plot_button(self):
        equi_volume_plotter = evp.EquiVolumePlotter(ticker=self.ticker_name.get("0.0", "end").strip(),
                                                    start_date=self.start_date_entry.get(),
                                                    end_date=self.end_date_entry.get(),
                                                    time_interval=self.time_interval_var.get(),
                                                    color=self.bar_color_var.get(),
                                                    hide_close_line=self.hide_close_line_var.get(),
                                                    hide_edge_line=self.hide_edge_line_var.get(),
                                                    data_src=self.data_source_var.get(),
                                                    tdx_dir=self.tdx_dir_text_box.get("0.0", "end").strip())
        equi_volume_plotter.plot_equivolume_chart()


if __name__ == "__main__":
    app = App()
    app.mainloop()
