import pandas as pd

data = pd.read_csv('thursdayNoon.csv', index_col=False)
labels = ['Flow Bytes/s', 'Total Length of Fwd Packets',
          ' Flow Duration', ' Fwd Packet Length Max', ' Label']

useful = data[labels]
useful.to_csv('thursdayNoonExtracted.csv', index=False)
