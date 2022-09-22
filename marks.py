import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def marks_prediction(marks):
    df = pd.read_csv("score.csv")

    X = df.iloc[:,:-1].values
    y = df.iloc[:,1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, test_size=0.2, random_state = 42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    X_test = np.array(marks)
    X_test = X_test.reshape(1, -1)
    
    return model.predict(X_test)

