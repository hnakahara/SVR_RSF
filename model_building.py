# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import set_config
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sksurv.datasets import load_gbsg2
from sksurv.preprocessing import OneHotEncoder
from sksurv.ensemble import RandomSurvivalForest
import warnings
warnings.simplefilter('ignore', FutureWarning)
set_config(display="text")  # displays text representation of estimators

# load matrix
file = "path/to/file.csv"
df = pd.read_csv(file)

# convert Event type
df = df.replace({'Event': {0: False, 1: True}})
df["Event"] = df["Event"].astype(bool)
df_tmp = df.loc[:,["Plt", "gamma-GTP", "male0", "age", "ALT", "Event", "time"]].dropna()

# Split into objective and dependent variables
y = [tuple(x) for x in df_tmp[["Event", "time"]].values]
y = np.array(pd.array(y), dtype = [('Event', '?'), ('time', 'i8')])

X = df_tmp.drop(["Event", "time"], axis = 1)

# Split into train and test datasets
random_state = 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=random_state)

# Run a random survival forest
rsf = RandomSurvivalForest(
    n_estimators=500, max_depth = 14, min_samples_split=8, min_samples_leaf=20, n_jobs=-1, random_state=random_state
)

rsf.fit(X_train, y_train)

# import library for saving model
import pickle

filename = 'path/to/rsf.sav'
pickle.dump(rsf, open(filename, 'wb'))
