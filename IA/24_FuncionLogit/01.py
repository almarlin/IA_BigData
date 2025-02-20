import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, auc


df = pd.read_csv("credit_approval_data.csv")

x = df.drop("Aprobado", axis=1)
y = df["Aprobado"]

X_train, X_test, y_train, y_test = train_test_split(
    x, y, random_state=42, test_size=0.2
)

scaler = StandardScaler()
x_train = scaler.fit_transform(X=X_train)
x_test = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

matrizConfusion = confusion_matrix(y_pred=y_pred, y_true=y_test)
print(f"Matriz de confusión:\n{matrizConfusion}")

report = classification_report(y_test, y_pred, target_names=["No aprobado", "Aprobado"])
print(f"Reporte de clasificación:\n{report}")

coef = model.coef_
coef_df = pd.DataFrame(coef.T, columns=['Coeficiente'], index=x.columns)
print(f"Coeficientes de las características:\n{coef_df}")

fpr, tpr, _ = roc_curve(y_test, model.predict_proba(x_test)[:, 1])
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