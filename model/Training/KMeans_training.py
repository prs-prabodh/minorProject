import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import numpy as np

data = pd.read_csv("extractedData.csv", index_col=False)
train, test = train_test_split(data, test_size=0.2)

x = train.drop(['Label'], axis=1)
y = train['Label']
y = (y == 1)

X = np.array(test.drop(['Label'], axis=1))
Y = np.array(test['Label'])
Y = (Y == 1)

x = np.array(x)
y = np.array(y)

normaliser = MinMaxScaler()
x = normaliser.fit_transform(x)
X = normaliser.fit_transform(X)

kmeans = KMeans(n_clusters=2)
kmeans.fit(x)

correct = 0
for i in range(len(X)):
    params = np.array(X[i])
    params = params. reshape(-1, len(params))
    prediction = kmeans.predict(params)
    if prediction[0] == Y[i]:
        correct += 1

print(correct/len(X))
