import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import joblib
from sklearn.decomposition import PCA
from sklearn import preprocessing
import os
root_directory = os.path.abspath('..')

if __name__ == '__main__':
    train = pd.read_csv(root_directory + '/data/training/train.csv', index_col='project_number')
    train.drop(['bid_days', 'engineers_estimate', 'start_date'], axis=1, inplace=True)

    y = np.array(train.iloc[:, -1])
    scale = preprocessing.MaxAbsScaler()
    X = scale.fit_transform(train.iloc[:, 0:-1])

    n_components = 537
    pca = PCA(n_components=n_components)
    X = pca.fit_transform(X)

    km = KMeans(n_clusters=2)
    km.fit(X)
    clusters = km.predict(X)

    joblib.dump(pca, root_directory + '/data/training/pickel/pca.pkl')
    joblib.dump(scale, root_directory + '/data/training/pickel/scale.pkl')
    joblib.dump(km, root_directory + '/data/training/pickel/km.pkl')
