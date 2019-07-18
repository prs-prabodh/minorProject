import pandas as pd
data = pd.read_csv("F:/Minor/New folder/combined.csv", index_col=False,low_memory = False , encoding = "cp1258")
print(data.shape)

attacks = data[(data[' Label'] == 1)|(data[' Label'] == 2)|(data[' Label'] == 3)|(data[' Label'] == 4)|(data[' Label'] == 5)|(data[' Label'] == 6)|(data[' Label'] == 7)|(data[' Label'] == 8)|(data[' Label'] == 9)|(data[' Label'] == 10)|(data[' Label'] == 11)|(data[' Label'] == 12)|(data[' Label'] == 13)|(data[' Label'] == 14)]
print("Attack data dimensions: ", attacks.shape)
normal = data[data[' Label'] == 0]
print("Normal data dimensions: ", normal.shape)
train = attacks.append(normal[:(2*attacks.shape[0])])
print("Extracted data dimensions: ", train.shape)
train = train.sample(frac=1)
train.to_csv('F:/Minor/New folder/filtered_combined.csv', index=False)
