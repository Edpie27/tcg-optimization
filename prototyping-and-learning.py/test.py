from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "sales.csv"
df = pd.read_csv(csv_path)

#remove singles from the transaction table
#df_no_card = df[df['kind'] != 'Card']
print(df.shape)