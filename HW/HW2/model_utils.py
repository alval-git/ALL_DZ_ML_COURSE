from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



def train_model(X, y):
  try:
    model = LinearRegression()
    model.fit(X, y)
    return model
  except Exception as e:
    print(f"train error: {e}")


def predict(model, X):
  try:
    return model.predict(X)
  except Exception as e:
    print(f"prediction error: {e}")


def evaluate_model(y_true, y_pred):
  try:
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, r2
  except Exception as e:
    print(f"evaluation error: {e}")


