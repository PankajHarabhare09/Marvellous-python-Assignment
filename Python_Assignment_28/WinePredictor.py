# Step 1: Get Data
# Step 2: Clean, Prepare and Manipulate Data
# Step 3: Train Data
# Step 4: Test Data
# Step 5: Calculate Accuracy

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def main():
    
    data = pd.read_csv('WinePredictor.csv')

    
    # Assuming the first column is the target class 
    X = data.iloc[:, 1:]  # Features
    y = data.iloc[:, 0]   # Target class

    # Feature Scaling 
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy of Wine Classifier:", accuracy)

if __name__ == "__main__":
    main()
