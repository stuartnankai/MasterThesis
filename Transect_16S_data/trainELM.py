from elm import ELM
from sklearn.preprocessing import normalize
from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
import tempfile
import pandas as pd



test_data_home = tempfile.mkdtemp()

db_name = 'australian'

data_set = pd.read_csv('australian.csv')
data_set_data = data_set.iloc[:, :-1]
df_norm = (data_set_data - data_set_data.mean()) / (data_set_data.max() - data_set_data.min())
print(df_norm)
y = data_set['class-label']

print(y)

X_train, X_test, y_train, y_test = train_test_split(
    df_norm, y, test_size=0.4)

elm = ELM(hid_num=10).fit(X_train, y_train)

print("ELM Accuracy %0.3f " % elm.score(X_test, y_test))