# SentinelAI
SentinelAI - A machine learning model that identifies fraudulent credit card transactions
## **Introduction**

This model aims to identify fraudulent credit card transactions using a RandomForestClassifier algorithm. The model takes in input features of credit card transactions and predicts whether the transaction is fraudulent or not.

## **Algorithm**

The RandomForestClassifier is a decision tree-based algorithm that randomly selects subsets of features and samples to build multiple decision trees. The final prediction is made by aggregating the results from all trees. This algorithm is commonly used in fraud detection because it can handle large datasets with many features and can identify patterns in data that may be indicative of fraud.

## **Dataset**

The dataset used for training and testing the model is a publicly available dataset called the "Credit Card Fraud Detection" dataset. This dataset contains credit card transactions made by European cardholders over a two-day period in September 2013. The dataset contains 284,315 transactions, of which 492 (0.172%) are fraudulent. The dataset contains 30 features, most of which are anonymized.

## **Data Preprocessing**

Before feeding the data into the model, the data underwent some preprocessing steps such as scaling and normalization. This is important to ensure that all features are in the same range and to prevent features with large values from dominating the model.

## **Feature Selection**

The feature selection was done by analyzing the correlation matrix between the features and the target variable. Only the relevant features were retained for the model.

## **Model Performance**

The model's performance was evaluated using accuracy, precision, recall, and F1-score. The model achieved an accuracy of 99.9%, a precision of 0.943, a recall of 0.761, and an F1-score of 0.844. The model's performance was further improved by hyperparameter tuning.

## **Conclusion**

The RandomForestClassifier algorithm is an effective method for detecting fraudulent credit card transactions. The model achieved a high level of accuracy and performance, which suggests it can be used in real-world applications for detecting fraud.

## **Date Created**
May 2023

## **Creator**
Gideon Ogunbanjo
