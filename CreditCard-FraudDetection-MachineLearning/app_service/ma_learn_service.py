# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
from matplotlib import pyplot
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
import numpy as np
data = pd.read_csv('qconlondon2016_sample_data.csv')
print data.head()
print type(data.head())
print data.fraudulent.value_counts()
print data.card_country.value_counts()

encoded_countries = pd.get_dummies(data.card_country, prefix='cc_')
data = data.join(encoded_countries)
y = data.fraudulent
X = data[['amount', 'card_use_24h', 'cc__AU', 'cc__GB']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
lr_model = LogisticRegression().fit(X_train, y_train)
lr_model.coef_
lr_model.intercept_
y_test_predict_lr = lr_model.predict_proba(X_test)
lr_model.classes_
y_test_predict_lr
y_test_scores_lr = [x[1] for x in y_test_predict_lr]
fpr, tpr, thresholds = roc_curve(y_test, y_test_scores_lr)
fpr[len(fpr)/2], tpr[len(tpr)/2], thresholds[len(thresholds)/2]
pyplot.plot(fpr, tpr, color='b')
pyplot.plot(np.linspace(0, 1, 11), np.linspace(0, 1, 11), color='r')
pyplot.xlabel("False Positive Rate")
pyplot.ylabel("True Positive Rate (Recall)")
roc_auc_score(y_test, y_test_scores_lr)
dt_model = DecisionTreeClassifier(
    max_depth=3, min_samples_split=20).fit(X_train, y_train)
y_test_scores_dt = [x[1] for x in dt_model.predict_proba(X_test)]
roc_auc_score(y_test, y_test_scores_dt)
rf_model = RandomForestClassifier(
    n_estimators=100, min_samples_leaf=100).fit(X_train, y_train)
y_test_scores_rf = [x[1] for x in rf_model.predict_proba(X_test)]
roc_auc_score(y_test, y_test_scores_rf)
export_graphviz(dt_model, 'tree.dot', feature_names=X.columns)
p = lambda L: (np.exp(0.5+L)/(1 + np.exp(0.5+L)))
x = np.linspace(-5, 5, 100)
y = map(p, x)
pyplot.plot(x, y)
pyplot.xlabel('L')
pyplot.ylabel('Probability')

