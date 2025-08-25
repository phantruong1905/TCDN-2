import os
import pandas as pd
from vnstock import Vnstock

# List of symbols you want
symbols = ['FPT', 'VNM', 'SCS']

# Output folder
out_folder = "dividends_data"
os.makedirs(out_folder, exist_ok=True)

# Loop through each symbol
for sym in symbols:
    try:
        company = Vnstock().stock(symbol=sym, source="TCBS").company
        df = company.dividends()

        # Save to CSV
        out_path = os.path.join(out_folder, f"{sym}_dividends.csv")
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

        print(f"✅ Saved {sym} dividends to {out_path}")
    except Exception as e:
        print(f"❌ Error fetching {sym}: {e}")
