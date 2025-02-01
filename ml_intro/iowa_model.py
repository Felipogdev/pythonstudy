import pandas as pd
import kagglehub


path = kagglehub.dataset_download("marcopale/housing")

print("Path to dataset files:", path)

iowa_df = pd.read_csv(f"{path}/AmesHousing.csv")

features = ['Total Bsmt SF', 'Gr Liv Area', 'Garage Area', '1st Flr SF', '2nd Flr SF', 'Lot Area', 'Year Built', 'Year Remod/Add']
X = iowa_df[features]
y = iowa_df.SalePrice


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
#Splitting my data to train
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

iowa_model = DecisionTreeRegressor(random_state = 1)

iowa_model.fit(train_X, train_y)

val_predicitons = iowa_model.predict(val_X)

from sklearn.metrics import mean_absolute_error

val_mae = mean_absolute_error(val_y, val_predicitons)
print(val_mae)