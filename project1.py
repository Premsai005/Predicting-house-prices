# -*- coding: utf-8 -*-
"""project1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IDCAgtqtHNicG2UJZuy5rX_1HoAea0Vc
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the training dataset
train_data = pd.read_csv('train.csv')

# Load the testing dataset
test_data = pd.read_csv('test.csv')

#preprocess training data
train_data.fillna(0, inplace=True)

# Feature selection for training
X_train = train_data[['LotArea', 'BedroomAbvGr', 'FullBath']]
y_train = train_data['SalePrice']

# Train the model using the training dataset
model = LinearRegression()
model.fit(X_train, y_train)

# Preprocess the testing dataset
test_data.fillna(0, inplace=True)

# features for testing the datasets
X_test = test_data[['LotArea', 'BedroomAbvGr', 'FullBath']]

# Make predictions
predicted_prices = model.predict(X_test)

# Add predicted prices to the testing dataset
test_data['PredictedPrice'] = predicted_prices

# Save the complete testing dataset with predictions
test_data.to_csv('predicted_prices.csv', index=False)

# Print the final Predicted values of each house
print(test_data)