
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

def main():
    # importing csv file
    data = pd.read_csv("diabetes.csv")

    line = "-"*54
    #Printing first 5 rows
    print(line)
    print("First 5 Rows")
    print(data.head())
    print(line)
    print(line+"\n")

    #prrinting column info and null values
    print(line)
    print(data.info())
    print(line)
    print(data.isnull().sum())
    print(line)
    print(line+"\n")

    #histogram
    data.hist(bins = 20 , figsize = (15 , 10))
    plt.tight_layout()
    plt.show()
    

    ColOfZeros = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    data[ColOfZeros] = data[ColOfZeros].replace(0 , np.nan)

    data.fillna(data.median() , inplace = True)

    X = data.drop("Outcome", axis=1)
    y = data["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train , X_test , Y_train  , Y_test = train_test_split(X_scaled , y , test_size = 0.2 , random_state = 42)

    #LOGESTICREGRESSION
    LogReg = LogisticRegression()
    LogReg.fit(X_train , Y_train)

    #KNN
    knn = KNeighborsClassifier()
    knn.fit(X_train , Y_train)

    #DECISIONTREECLASSIFIER
    DecTree = DecisionTreeClassifier()
    DecTree.fit(X_train , Y_train)


    models = {"Logestic Regression" : LogReg , "KNeighborClassifier" : knn , "Decision Tree Classifier" : DecTree}

    for name , model in models.items():
        print(line)
        print("Model: -->" , name)
        print(line)

        Y_predict = model.predict(X_test)
        print("Accuracy", accuracy_score(Y_test , Y_predict)*100)
        print("Precision", precision_score(Y_test , Y_predict)*100)
        print("Recall", recall_score(Y_test , Y_predict)*100)
        print("F1 Score", f1_score(Y_test , Y_predict)*100)

    ConMat = confusion_matrix(Y_test , Y_predict)
    ConfusionMatrixDisplay(confusion_matrix = ConMat).plot()
    plt.title(name)
    plt.show()

    
if __name__ == "__main__":
    main()