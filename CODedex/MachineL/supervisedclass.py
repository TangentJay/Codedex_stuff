import pandas as pd
import sklearn.datasets
import sklearn.neighbors

data = sklearn.datasets.load_breast_cancer()

#load data into dataframe
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

#get the first 500 tumors
X = df.drop(columns='target').iloc[:500]
y = df['target'].iloc[:500]


my_model = sklearn.neighbors.KNeighborsClassifier()
my_model.fit(X,y)

row_501 = df.drop(columns='target').iloc[[500]]

prediction = my_model.predict(row_501)
print(prediction)
print(row_501)
