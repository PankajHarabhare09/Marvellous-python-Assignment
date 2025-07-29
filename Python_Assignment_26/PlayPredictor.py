# Step 1: Load data
# Step 2: Convert text to numbers
# Step 3: Train model using full data
# Step 4: Predict (e.g., Rainy, Mild)
# Step 5: Accuracy check

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def main():
    data = pd.read_csv("PlayPredictor.csv")

    le = LabelEncoder()
    data['Whether'] = le.fit_transform(data['Whether'])
    data['Temperature'] = le.fit_transform(data['Temperature'])
    data['Play'] = le.fit_transform(data['Play'])

    # Features and Target
    X = data[['Whether', 'Temperature']]
    y = data['Play']


    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X, y)

    print("Label mapping for Wether:", list(le.classes_))

    # Predict
    prediction = model.predict([[2, 2]])  
    #print("Prediction:", "Yes" if prediction[0] == 1 else "No")

    if prediction[0] == 1:
        print("yes")
    else:
        print("no")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print("Accuracy:", accuracy*100)

if __name__ == "__main__":
    main()
