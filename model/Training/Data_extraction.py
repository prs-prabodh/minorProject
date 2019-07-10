import pandas as pd

data = pd.read_csv('thursdayNoon.csv', index_col=False)
labels = [' Flow Duration', ' Total Fwd Packets',
          ' Flow Packets/s', ' Flow IAT Min', ' Label']

useful = data[labels]
useful.to_csv('thursdayNoonExtracted.csv', index=False)
