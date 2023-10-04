from datetime import datetime
import io
from pathlib import Path
import tempfile
import zipfile
import requests
import pandas as pd

from cot_client.header import headers
from typing import NamedTuple


class Event(NamedTuple):
    market_and_exchange_names: str
    cftc_commodity_code: int
    report_date: str
    open_interest_all: float
    prod_merc_positions_long_all: float
    prod_merc_positions_short_all: float
    swap_positions_long_all: float
    swap_positions_short_all: float
    m_money_positions_long_all: float
    m_money_positions_short_all: float
    other_rept_positions_long_all: float
    other_rept_positions_short_all: float
    nonrept_positions_long_all: float
    nonrept_positions_short_all: float
    kind: str = "COMMITMENT_OF_TRADERS"


def row_to_event(row: pd.Series, report_date_column_name: str) -> Event:
    report_date = row[report_date_column_name]
    if pd.isna(report_date):
        report_date = row["Report_Date_as_MM_DD_YYYY"]

        if pd.isna(report_date):
            raise ValueError(row)

    return Event(
        market_and_exchange_names=row["Market_and_Exchange_Names"],
        cftc_commodity_code=row["CFTC_Commodity_Code"],
        report_date=report_date,
        open_interest_all=row["Open_Interest_All"],
        prod_merc_positions_long_all=row["Prod_Merc_Positions_Long_All"],
        prod_merc_positions_short_all=row["Prod_Merc_Positions_Short_All"],
        swap_positions_long_all=row["Swap_Positions_Long_All"],
        swap_positions_short_all=row["Swap__Positions_Short_All"],
        m_money_positions_long_all=row["M_Money_Positions_Long_All"],
        m_money_positions_short_all=row["M_Money_Positions_Short_All"],
        other_rept_positions_long_all=row["Other_Rept_Positions_Long_All"],
        other_rept_positions_short_all=row["Other_Rept_Positions_Short_All"],
        nonrept_positions_long_all=row["NonRept_Positions_Long_All"],
        nonrept_positions_short_all=row["NonRept_Positions_Short_All"],
    )


def latest_cot_report() -> pd.DataFrame:
    """Downloads and returns the latest disaggregated Commitment of Traders report."""
    for _, row in pd.read_csv(
        io.BytesIO(
            requests.get("https://www.cftc.gov/dea/newcot/c_disagg.txt").content
        ),
        names=headers(),
    ).iterrows():
        yield row_to_event(row, report_date_column_name="As_of_Date_Form_YYYY-MM-DD")


def historical_cot_report() -> pd.DataFrame:
    """Downloads the all historical data."""

    def load_combine_reports_per_year(year: int) -> pd.DataFrame:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = Path(temp_dir)
            zip_file_url = (
                f"https://www.cftc.gov/files/dea/history/com_disagg_txt_{year}.zip"
            )
            r = requests.get(zip_file_url)

            with zipfile.ZipFile(io.BytesIO(r.content)) as zip_ref:
                zip_ref.extractall(temp_dir)

            return pd.read_csv(temp_dir / "c_year.txt", low_memory=False)

    def load_combine_reports_since_year(year: int) -> pd.DataFrame:
        dfs = []

        for dt in range(year, datetime.today().year + 1):
            dfs.append(load_combine_reports_per_year(dt))

        return pd.concat(dfs)

    for _, row in load_combine_reports_since_year(2010).iterrows():
        yield row_to_event(row, report_date_column_name="Report_Date_as_YYYY-MM-DD")
