from sklearn.neighbors import KNeighborsClassifier
import joblib as jl
import os

# print(os.getcwd())

trained_model = jl.load('model/Training/trained_model.pkl')


def trainModel(data, label):
    model = KNeighborsClassifier(n_neighbors=k, algorithm='auto')
    model.fit(data, label)

    return model


def getPrediction(data):
    prediction = trained_model.predict(data)

    return prediction


def analyze(packet_data):
    # analyze packet
    result = getPrediction(packet_data)

    return result == 0
