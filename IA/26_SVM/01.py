import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import auc, confusion_matrix, classification_report, roc_curve
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import AllKNN

# Cargar los datos
df = pd.read_csv("fraude_data.csv")

X = df.drop("Fraude", axis=1)  
y = df["Fraude"]  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


allknn = AllKNN(n_neighbors=3, allow_minority=True)
X_train_reduced, y_train_reduced = allknn.fit_resample(X_train, y_train)


smote = SMOTE(random_state=42)
X_train_final, y_train_final = smote.fit_resample(X_train_reduced, y_train_reduced)

print("Distribución antes del balanceo:", y_train.value_counts())
print("Distribución después del balanceo:", y_train.value_counts())

model = SVC(kernel='rbf', C=1, gamma='scale', probability=True)
model.fit(X_train_final, y_train_final)


y_pred = model.predict(X_test)


print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred, target_names=["No fraude", "Fraude"]))


fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color="darkorange", lw=2, label="Curva ROC (area = %0.2f)" % roc_auc)
plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("Tasa de Falsos Positivos")
plt.ylabel("Tasa de Verdaderos Positivos")
plt.title("Curva ROC")
plt.legend(loc="lower right")
plt.show()
