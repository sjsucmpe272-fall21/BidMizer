import pandas as pd
from sklearn.model_selection import train_test_split
import os
root_directory = os.path.abspath('..')

if __name__ == '__main__':
    df = pd.read_csv(root_directory + '/data/main_data.csv', index_col='project_number')
    # df.drop(['engineers_estimate','bid_days','start_date'],inplace=True,axis=1)
    train, test = train_test_split(df, random_state=10)
    train.to_csv(root_directory + '/data/training/train.csv')
    test.to_csv(root_directory + '/data/training/test.csv')
