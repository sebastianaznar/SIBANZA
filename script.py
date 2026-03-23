import yfinance as yf
import pandas as pd

ticker_symbol = "BTC-USD"

data = yf.download(
    ticker_symbol,
    period="5d",
    interval="1d",
    progress=False
)

if data.empty:
    print("No hay datos disponibles.")
else:
    # Aplanar columnas si vienen como MultiIndex
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Tomar solo la última fila
    row = data.tail(1).reset_index()

    # Construir fila final manualmente (sin arrays 2D)
    date_str = row.loc[0, "Date"].strftime("%Y-%m-%d")

    final_df = pd.DataFrame([{
        "asset_id": f"{ticker_symbol}_{date_str}",
        "ticker": ticker_symbol,
        "date": date_str,
        "Open": row.loc[0, "Open"],
        "High": row.loc[0, "High"],
        "Low": row.loc[0, "Low"],
        "Close": row.loc[0, "Close"],
        "Volume": row.loc[0, "Volume"]
    }])

    final_df.to_csv("data_ticker.csv", index=False)

    print("Archivo generado correctamente:")
    print(final_df)