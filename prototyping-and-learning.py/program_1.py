from pathlib import Path
csv_path = Path(__file__).parent.parent / "sales.csv"

import pandas as pd
tcg = pd.read_csv(csv_path)

tcg = tcg[tcg['kind'] != 'Card']
rev = tcg.loc[:,['name','revenue','units']]
name = rev['name']
rm = rev.revenue / rev.units #this is equal to the best price but with a more
# concise name

final = pd.DataFrame({"item_name": name,"Revenue/Unit" : rm})

import matplotlib.pyplot as plt
final.plot(x='item_name',y='Revenue/Unit',kind='barh')
plt.show()
