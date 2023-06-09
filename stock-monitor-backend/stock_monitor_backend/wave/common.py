from h2o_lightwave import data, ui


def preprocess_dataframe(df):
    new_df = df.reset_index()
    new_df["Date"] = new_df["Date"].apply(lambda el: el.isoformat(timespec="minutes"))

    return new_df


def color_stock_dataframe(df):
    df["Color"] = df[["Open", "Close"]].apply(lambda el: "green" if el["Open"] < el["Close"] else "red",
                                              axis=1)
    return df


def dataframe_to_data(df):
    return data(df.columns.to_list(), df.shape[0], rows=df.values.tolist(), pack=True)


def stock_graph(stock, box='1 3 11 5', with_summary=False):
    assert not stock.history.empty, stock.ticker_name
    graph_data = dataframe_to_data(
        color_stock_dataframe(
            preprocess_dataframe(stock.history))[
            ["Date", "Low", "High", "Open", "Close", "Color", "Volume"]])
    items = [
        ui.text_xl(stock.ticker_name),
        ui.visualization(
            name='stock',
            height="260px",
            data=graph_data,
            plot=ui.plot(
                [ui.mark(type='schema',
                         x_scale='time',
                         x='=Date',
                         y_q1="={{intl Open notation='compact' compactDisplay='short'}}",
                         y_q2="={{intl Open notation='compact' compactDisplay='short'}}",
                         y_q3="={{intl Close notation='compact' compactDisplay='short'}}",
                         y1="={{intl Low notation='compact' compactDisplay='short'}}",
                         y2="={{intl High notation='compact' compactDisplay='short'}}",
                         y_nice=True,
                         color="=Color",
                         color_range="#06982d #ae1325",
                         color_domain=["green", "red"])])),
        ui.visualization(
            name='volume',
            height="100px",
            data=graph_data,
            plot=ui.plot(
                [ui.mark(type='interval', x_scale='time', x='=Date',
                         y_scale="quantile",
                         y="={{intl Volume notation='compact' compactDisplay='short'}}",
                         color="=Color",
                         y_nice=True,
                         color_range="#06982d #ae1325",
                         color_domain=["green", "red"])
                 ])),
    ]
    if with_summary:
        items.append(ui.text_s(stock.business_summary))
    return ui.form_card(
        box=box,
        items=items
    )
