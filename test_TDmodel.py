import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\hiennpd3\OneDrive - VPBank\AA Team\2. TD forecast model\3. Architecture\Package\test_TDmodel.csv')

# Preprocess timestamp column (PERIOD)
df['PERIOD'] = pd.to_datetime(df['PERIOD'])  # Convert to datetime data type
df['Year'] = df['PERIOD'].dt.year  # Extract year as a feature
df['Month'] = df['PERIOD'].dt.month  # Extract month as a feature

categorical_cols = ['PRODUCT_GROUP', 'movement_type', 'Term_CM', 'Term_LM', 'Currency_2', 'TD_type']

# Encode categorical variables using one-hot encoding
encoded_df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)   

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

# Prepare the input features (X) and target variable (y)
X = encoded_df.drop(['EOP_CM', 'PERIOD'], axis=1)
y = encoded_df['EOP_CM']

X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=1000)
model = LinearRegression()  
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
mean_squared_error(y_test,y_pred)

from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

# Prepare the input features (X) and target variable (y)
X = encoded_df.drop(['EOP_CM', 'PERIOD'], axis=1)
y = encoded_df['EOP_CM']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1000)

# Fit the ARIMA model
model = ARIMA(y_train, order=(3, 1, 3))  # Replace p, d, q with appropriate values
model_fit = model.fit()

# Make predictions
y_pred = model_fit.predict(start=len(y_train), end=len(y_train) + len(y_test) - 1)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
