# Step 1: Load Data
# Step 2: Prepare Data
# Step 3: Split the Data 
# Step 4: Train the Model
# Step 5: Predict & Display Results

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():
    data = pd.read_csv("Advertising.csv")

    X = data[['TV', 'radio', 'newspaper']]  # Features
    y = data['sales']  # Target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    model = LinearRegression()
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)

    # Display predicted vs actual
    result = pd.DataFrame({'Predicted': y_pred, 'Actual': y_test.values})
    print(result)

if __name__ == "__main__":
    main()
