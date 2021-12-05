import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import r2_score, mean_squared_error
import joblib
import os
root_directory = os.path.abspath('..')

class helper(object):

    def __init__(self):
        self.colors = {'r2': 'r', 'mse': 'g', 'mape': 'b'}

    def _emptydf(self, name):
        columns = ['r2', 'mse', 'mape']
        df = pd.DataFrame(columns=columns, index=range(1, len(self.param_values) + 1))
        df['index'] = df.index
        df['param_values'] = self.param_values
        df.index.name = name
        return df

    def mape(self, y_true, y_pred):
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    def score_model(self, y_true, y_pred=None, need_pred=False,
                    model=None, xg_boost=False):
        if need_pred:
            if xg_boost:
                X = xgb.DMatrix(X)
            y_pred = model.predict(X)
        return [r2_score(y_true, y_pred),
                mean_squared_error(y_true, y_pred),
                self.mape(y_true, y_pred)]
