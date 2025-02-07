from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

def get_mae (max_leaves_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaves_nodes, random_state= 0)
    model.fit(train_X,train_y)
    predictions_val= model.predict(val_X)
    mae = mean_absolute_error(val_y, predictions_val)
    return mae