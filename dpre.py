import pandas as pd
from sklearn.decomposition import PCA
from load import diabetes_df

# Data Cleaning
# Task 1: Handle Missing Values
diabetes_df.fillna(diabetes_df.mean(), inplace=True)

# Task 2: Remove Duplicates
diabetes_df.drop_duplicates(inplace=True)

# Data Transformation
# Task 1: Standardization of Numerical Features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
numerical_features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
diabetes_df[numerical_features] = scaler.fit_transform(diabetes_df[numerical_features])


# Task 2: Encoding Categorical Features (if applicable)
# Example: diabetes_df['gender'] = diabetes_df['gender'].map({'Male': 1, 'Female': 0})

# Data Reduction
# Task 1: Principal Component Analysis (PCA)
pca = PCA(n_components=2)
pca_result = pca.fit_transform(diabetes_df[numerical_features])
diabetes_df['PCA1'] = pca_result[:, 0]
diabetes_df['PCA2'] = pca_result[:, 1]

# Task 2: Feature Selection (Select relevant features based on domain knowledge)

# Data Discretization
# Task 1: Discretize Age into Age Groups
age_bins = [0, 30, 50, 80]
age_labels = ['Young', 'Adult', 'Senior']
diabetes_df['AgeGroup'] = pd.cut(diabetes_df['Age'], bins=age_bins, labels=age_labels)

# Task 2: Discretize BMI into BMI Categories (customize as needed)

# Save the resulting data frame as 'res_dpre.csv'
diabetes_df.to_csv('res_dpre.csv', index=False)