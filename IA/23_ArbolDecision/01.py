import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
from sklearn.metrics import roc_curve, auc
from imblearn.under_sampling import AllKNN
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import RandomOverSampler

df = pd.read_csv("clientes_marketing.csv")

x = df.drop("Compra", axis=1)
y = df["Compra"]

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)


scaler = StandardScaler()
x_train = scaler.fit_transform(X_train)
x_test = scaler.transform(X_test)

ros = RandomOverSampler(random_state=42)
x_train_oversampled, y_train_oversampled = ros.fit_resample(x_train, y_train)

# Aplicar AllKNN y Smote para balancear clases
allknn = AllKNN(n_neighbors=3, allow_minority=True)
X_train_reduced, y_train_reduced = allknn.fit_resample(x_train_oversampled, y_train_oversampled)

# Aplicamos SMOTE después
smote = SMOTE(random_state=42)
x_train_final, y_train_final = smote.fit_resample(X_train_reduced, y_train_reduced)



model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=15,
    max_features="sqrt",
    class_weight='balanced'
)
model.fit(x_train_final,y_train_final)

# Evaluar con el mejor modelo
y_pred = model.predict(x_test)
precision = accuracy_score(y_test, y_pred)
print(f"Mejor precisión: {precision:.3f}")
print(classification_report(y_test, y_pred, target_names=["No compra", "Compra"]))
print(confusion_matrix(y_test,y_pred))

coef = model.feature_importances_
coef_df = pd.DataFrame(coef.T, columns=['Importancia'], index=x.columns)
print(f"Importancia de las características:\n{coef_df}")

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
plot_tree(model)
plt.show()

