import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import numpy as np

""" Your Task

    Download and import the Data Science Job Salary dataset.
    Normalize the ‘salary’ column using Min-Max normalization which scales all salary values between 0 and 1.
    Implement dimensionality reduction like Principal Component Analysis (PCA) or t-SNE to reduce the number of features (columns) in the dataset.
    Group the dataset by the ‘experience_level’ column and calculate the average and median salary for each experience level (e.g., Junior, Mid-level, Senior).
 """

dataset = pd.read_csv(r"datascience_salaries.csv")
