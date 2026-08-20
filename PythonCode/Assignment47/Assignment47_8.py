

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
import joblib
def MarvellosRegration():
    Border = "-"*30
    print(Border)
    print("test the train maodel")
    print(Border)
    model = joblib.load("ASSignment47_7.pkl")
    print("model loded sucessfully")
    Marks = pd.DataFrame([{
        "Study Hours" :  6
    }])

    Y_pred = model.predict(Marks)
 
    print("predicted anser")
    print(Y_pred[:3])

def main():
    MarvellosRegration()

if __name__ == "__main__":
    main()