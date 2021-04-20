import numpy as np
import pandas as pd

import tools

from sklearn.model_selection import train_test_split

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# Leer los datos unidos
unidos = pd.read_csv("unidos.csv")
# Y = mX + b  :: Y = wX + b
y = np.where(unidos['Gdp'] > 0.25, 1, 0)

x = unidos
x.drop('Gdp', axis=1, inplace=True)
print(y)
tools.mostrar_info(x, 'x')

# Separar los datos
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.176)

# ===========================================================

print('== Algunos clasificadores ==')
#print('Regresión logística')
logReg = LogisticRegression()
logReg.fit(x_train, y_train)
y_predict = logReg.predict(x_val)
print('Precisión Regresión logística', logReg.score(x_train, y_train))

#print('SVM')
svm = SVC()
svm.fit(x_train, y_train)
y_predict = svm.predict(x_val)
print('Precisión SVM', svm.score(x_train, y_train))
#print(y_predict)
#print(y_val)
#comparativa = y_val

#print('KNN')
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
y_predict = knn.predict(x_val)
print('Precisión KNN', knn.score(x_train, y_train))

#print('ElasticNet')
en = ElasticNet()
en.fit(x_train, y_train)
y_predict = en.predict(x_val)
print('Precisión ElasticNet', en.score(x_train, y_train))

rl = LinearRegression()
rl.fit(x_train, y_train)
y_predict = rl.predict(x_val)
print('Precisión LinearRegression', rl.score(x_train, y_train))

# == Validación cruzada ==
print(' ========== Validación cruzada ========== ')
# Test Options and Evaluation Metrics
num_folds = 10
scoring = "neg_mean_squared_error" # https://scikit-learn.org/stable/modules/model_evaluation.html
# Cargar algoritmos
models = []
models.append(('SVC', SVC()))
models.append(('LogR', LogisticRegression()))
models.append(('LR', LinearRegression()))
models.append(('LASSO', Lasso()))
models.append(('EN', ElasticNet()))
models.append(('KNN', KNeighborsRegressor()))
models.append(('CART', DecisionTreeRegressor()))
models.append(('SVR', SVR()))
results = []
names = []
seed = 1
kfold = KFold(n_splits=num_folds, random_state=None)
for name, model in models:
    cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(),   cv_results.std())
    print(msg)



# Compare Algorithms
from matplotlib import pyplot
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()


print('Ver: https://scikit-learn.org/stable/user_guide.html')
