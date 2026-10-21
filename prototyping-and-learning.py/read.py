#Use pathlib to import Path
from pathlib import Path

#import pandas using an alias
import pandas as pd

#use the path command to make the program find a file called "sales.csv" in all
#directories
csv_path = Path(__file__).with_name("sales.csv")

#tell pandas to read the csv
df = pd.read_csv(csv_path)

#use the .to_string suffix to ensure the entire table is printed. Since our
#table is small, we do not need to limit the size of it.
print(df.to_string())