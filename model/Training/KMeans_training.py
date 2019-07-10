import pandas as pd
import joblib as jl
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

data = pd.read_csv("thursdayNoonPrepared.csv", index_col=False)
train, test = train_test_split(data, test_size=0.2)

x = np.array(train.drop([' Label'], axis=1))
y = np.array(train[' Label'])

# Classify all types of attacks into one superclass ATTACK
y = (y >= 1)

X = np.array(test.drop([' Label'], axis=1))
Y = np.array(test[' Label'])

# Classify all types of attacks into one superclass ATTACK
Y = (Y >= 1)

normaliser = MinMaxScaler()
x = normaliser.fit_transform(x)
X = normaliser.fit_transform(X)

kmeans = KMeans(n_clusters=2)
kmeans.fit(x)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(x, y)

correctKmeans = 0
correctKnn = 0
for i in range(len(X)):
    params = np.array(X[i])
    params = params. reshape(-1, len(params))
    prediction = kmeans.predict(params)
    if prediction[0] == Y[i]:
        correctKmeans += 1
    prediction = knn.predict(params)
    if prediction[0] == Y[i]:
        correctKnn += 1

print("KMeans Accuracy: ", correctKmeans/len(X))
print("KNN Accuracy: ", correctKnn/len(X))
jl.dump(knn, 'trained_model.pkl')
