import pandas as pd
data = pd.read_csv("F:/Minor/New folder/cleaned_portScan.csv", index_col=False)
print(data.shape)
attacks = data[(data[' Label'] == 13)]
print("Attack data dimensions: ", attacks.shape)
normal = data[data[' Label'] == 0]
print("Normal data dimensions: ", normal.shape)
train = attacks.append(normal[:(2*attacks.shape[0])])
print("Extracted data dimensions: ", train.shape)
train = train.sample(frac=1)
train.to_csv('F:/Minor/New folder/filtered_portScan.csv', index=False)
