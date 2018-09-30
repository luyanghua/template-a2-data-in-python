import numpy as np
import pandas as pd

iris_dataset = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

iris = np.recfromcsv(iris_dataset, encoding=None)  # in numpy
iris = pd.read_csv(iris_dataset)  # in pandas

iris_setosa = iris['species'] == "setosa"
iris_versicolor = iris['species'] == "versicolor"
iris_virginica = iris['species'] == "virginica"

print(iris[iris_setosa].mean())
print(iris[iris_versicolor].mean())
print(iris[iris_virginica].mean())

print(iris[iris_setosa].std())
print(iris[iris_versicolor].std())
print(iris[iris_virginica].std())
