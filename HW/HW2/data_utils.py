import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer


def load_data(file_path, sep):
    try:
        return pd.read_csv(file_path, sep=sep)
    except FileNotFoundError:
        print("file was not found")


def preprocess_data(df, target_column, numeric_params):
  try:
    X = df.drop(columns=[target_column], axis=1)
    y = df[target_column]
    numeric_scaler = StandardScaler()
    preprocessor = ColumnTransformer(transformers=[('num', numeric_scaler, numeric_params)])
    X_processed = preprocessor.fit_transform(X)
    return X_processed, y, preprocessor
  
  except Exception as e:
    print(f"An error occurred: {e}")
    print(f"Exception type: {type(e)}")
      

def get_df_info(df):
   print("dataset info and example:")
   print(df.describe())
   print(df)