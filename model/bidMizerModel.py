import struct

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn import preprocessing
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor, ExtraTreesRegressor
from model.helper import helper
import os
root_directory = os.path.abspath('.')


class bidMizerModel(helper):

    def __init__(self, current_directory, scale=preprocessing.Normalizer(), date_scale=100,
                 n_clusters=5):
        self.std = scale
        self.date_scale = date_scale
        self.n_clusters = n_clusters
        self.current_directory = current_directory

    def _add_prediction(self, model, X):
        pred = model.predict(X)
        return np.hstack((X, pred.reshape(pred.shape[0], 1)))

    def fit(self, X, y):
        etr = ExtraTreesRegressor(n_estimators=25)
        etr.fit(X, y)
        joblib.dump(etr, root_directory + '/data/training/pickel/regresson1.pkl')
        X = self._add_prediction(etr, X)

        gbr = GradientBoostingRegressor(loss='lad')
        gbr.fit(X, y)
        joblib.dump(gbr, root_directory + '/data/training/pickel/regresson2.pkl')
        X = self._add_prediction(gbr, X)

        parameters = {'max_depth': 7, 'silent': 1, 'eta': 0.3, 'booster': 'gbtree'}
        dmat = xgb.DMatrix(X, label=y)
        self.xgb_model = xgb.train(parameters, dmat)
        joblib.dump(self.xgb_model, self.current_directory + '/data/training/pickel/xgb1.pkl')

    def predict(self, X):
        etr = joblib.load(self.current_directory + '/data/training/pickel/regresson1.pkl')
        gbr = joblib.load(self.current_directory + '/data/training/pickel/regresson2.pkl')
        self.xgb_model = joblib.load(root_directory + '/data/training/pickel/xgb1.pkl')

        X = self._add_prediction(etr, X)
        X = self._add_prediction(gbr, X)
        return self.xgb_model.predict(xgb.DMatrix(X))


if __name__ == '__main__':
    train = pd.read_csv(root_directory + '/data/training/train.csv', index_col='project_number')
    data_top = train.head()
    X = train.drop(['bid_days', 'bid_total', 'engineers_estimate', 'start_date'], axis=1)
    y = train.bid_total
    estimate = train.engineers_estimate
    X_train, X_test, y_train, y_test, estimate_train, estimate_test = train_test_split(X, y, estimate, random_state=10)

    model = bidMizerModel(root_directory)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(model.score_model(y_test, y_pred))
