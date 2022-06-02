import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

data = pd.read_csv('second_result.csv', dtype={'Unnamed: 0':str})

cancer = []
control = []
for el in data[:0].columns:
    if 'cncr' in el:
        cancer.append(el)

    if 'cntrl' in el:
        control.append(el)


cancer_values = np.transpose(data[cancer].values, axes=None)
control_values = np.transpose(data[control].values, axes=None)

y_cancer = [1 for i in range(len(cancer_values))]
y_control = [0 for i in range(len(control_values))]

x = np.concatenate((cancer_values, control_values), axis=0)
y = y_cancer + y_control

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.25, random_state = 0)
logreg = LogisticRegression(random_state=0)
logreg.fit(xtrain, ytrain)
y_pred = logreg.predict(xtest)

# [[True Positive, False Positive], [False Negative, True Negative]]
cm = confusion_matrix(ytest, y_pred)
print(cm)
print ("Accuracy : ", accuracy_score(ytest, y_pred))

print(xtest)
print(y_pred)
