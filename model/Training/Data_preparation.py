import pandas as pd
data = pd.read_csv("thursdayNoonExtracted.csv", index_col=False)
print(data.shape)
attacks = data[(data[' Label'] == 1) | (
    data[' Label'] == 2) | (data[' Label'] == 3)]
print("Attack data dimensions: ", attacks.shape)
normal = data[data[' Label'] == 0]
print("Normal data dimensions: ", normal.shape)
train = attacks.append(normal[:(2*attacks.shape[0])])
print("Extracted data dimensions: ", train.shape)
train = train.sample(frac=1)
train.to_csv('thursdayNoonPrepared.csv', index=False)
