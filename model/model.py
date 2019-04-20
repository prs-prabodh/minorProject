from sklearn.neighbors import KNeighborsClassifier

def trainModel(data, label):
    model = KNeighborsClassifier(n_neighbors=k, algorithm='auto')
    model.fit(data, label)

    return model

def getPrediction(data):
    prediction = model.predict(data)

    return prediction

def analyze(packet):
    # analyze packet

    return True, 'None', 'Nil'
