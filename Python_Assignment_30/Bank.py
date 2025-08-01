import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report , roc_auc_score , roc_curve

def main():
    line = "-"*54
    data = pd.read_csv("bank-full.csv", sep=';')

    #basic Info
    print(data.info())
    print(line,"\n")
    print(data.head())
    print(line,"\n")

    # Check for 'unknown' values in categorical features
    for col in data.select_dtypes(include = 'object').columns:
        print(line)
        print(f"{col} --> {data[col].value_counts()}")
        print(line)

    # Replace 'unknown' with most frequent value
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].replace('unknown' , data[col].mode()[0])

    le = LabelEncoder()
    for col in data.select_dtypes(include = 'object').columns:
        data[col] = le.fit_transform(data[col])

    ss = StandardScaler()

    ColOfNum = ['age', 'balance', 'day', 'duration', 'campaign', 'previous']
    data[ColOfNum] = ss.fit_transform(data[ColOfNum])

    X = data.drop('y' , axis = 1)
    y = data['y']

    X_train , X_test , Y_train , Y_test = train_test_split(X , y ,test_size = 0.2 , random_state = 42)

    #LogisticRegression
    LogReg = LogisticRegression(max_iter = 1000)
    LogReg.fit(X_train , Y_train)

    #KNN
    knn = KNeighborsClassifier()
    knn.fit(X_train , Y_train)

    #RandomForestClassifier
    RandFor = RandomForestClassifier()
    RandFor.fit(X_train , Y_train)

    models = {"LogisticRegression" : LogReg , "KNeighborsClassifier" : knn , "RandomForestClassifier" : RandFor}

    for name , model in models.items():
        Y_predict = model.predict(X_test)
        Y_prob = model.predict_proba(X_test)[: , 1]
        print(f"\n{name} Evaluation:")
        print("Accuracy: ",accuracy_score(Y_test , Y_predict)*100)
        print("Confusion Matrix \n: ",confusion_matrix(Y_test , Y_predict)*100)
        print("Classification Report \n: ",classification_report(Y_test , Y_predict)*100)
        print("Roc-AUC Score \n: ",roc_auc_score(Y_test , Y_predict)*100)

    for name , model in models.items():
        Y_predict = model.predict(X_test)
        cm = confusion_matrix(Y_test , Y_predict)
        sns.heatmap(cm , annot = True , fmt = 'd' , cmap = 'Blues')
        plt.title(f'{name} - Confusion Matrix')
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()

    for name , model in models.items():
        Y_predict = model.predict_proba(X_test)[: , 1]
        fpr , tpr , val = roc_curve(Y_test, Y_prob)
        plt.plot(fpr, tpr, label=name)

    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()