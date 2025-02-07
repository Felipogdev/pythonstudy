from sklearn.metrics import mean_absolute_error
import pandas as pd
import kagglehub
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from get_mae import get_mae 

path = kagglehub.dataset_download("marcopale/housing")

print("Path to dataset files:", path)

iowa_df = pd.read_csv(f"{path}/AmesHousing.csv")

features = ['Total Bsmt SF', 'Gr Liv Area', 'Garage Area', '1st Flr SF', '2nd Flr SF', 'Lot Area', 'Year Built', 'Year Remod/Add']
X = iowa_df[features]
y = iowa_df.SalePrice

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

iowa_model = DecisionTreeRegressor(random_state = 1)

iowa_model.fit(train_X, train_y)

val_predicitons = iowa_model.predict(val_X)

val_mae = mean_absolute_error(val_y, val_predicitons)
print(val_mae)

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
best_mae = float("inf")
best_tree_size=None

for max_leaf_nodes in candidate_max_leaf_nodes:
    temp_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    if temp_mae < best_mae:
        best_mae = temp_mae
        best_tree_size = max_leaf_nodes

final_model = DecisionTreeRegressor(max_leaf_nodes = best_tree_size, random_state = 1)
final_model.fit(X, y)
final_model_predictions = final_model.predict(val_X)
final_model_val_mae = mean_absolute_error(val_y, final_model_predictions)
print(final_model_val_mae)

