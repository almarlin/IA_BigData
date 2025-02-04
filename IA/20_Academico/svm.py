import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, label_binarize
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc, roc_auc_score
from sklearn.inspection import permutation_importance
from imblearn.under_sampling import AllKNN
from imblearn.over_sampling import SMOTE
from sklearn.inspection import permutation_importance

# Cargar y preparar datos
df_cardiaca = pd.read_csv("Dataset_Academico.csv")
X = df_cardiaca.drop("rendimiento_academico", axis=1)
y = df_cardiaca["rendimiento_academico"]

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar datos
scaler = StandardScaler()
x_train = scaler.fit_transform(X_train)
x_test = scaler.transform(X_test)

# Binarizar etiquetas
y_bin = label_binarize(y, classes=np.unique(y))
n_classes = y_bin.shape[1]

# Balancear clases
allknn = AllKNN(n_neighbors=3, allow_minority=True)
X_train_reduced, y_train_reduced = allknn.fit_resample(x_train, y_train)
smote = SMOTE(random_state=42)
X_train_final, y_train_final = smote.fit_resample(X_train_reduced, y_train_reduced)


# Crear y entrenar modelo
svm_model = SVC(kernel='rbf', C=1, gamma='scale', probability=True)
svm_model.fit(X_train_final, y_train_final)

# Predecir
y_pred = svm_model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# Matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nMatriz de confusión:")
print(conf_matrix)

# Reporte de clasificación
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

# Importancia de características
result = permutation_importance(svm_model, x_test, y_test, n_repeats=10, random_state=42, n_jobs=1)
coef_df = pd.DataFrame(result.importances_mean, columns=['Importancia'], index=X.columns)
print(f"\nImportancia de las características:\n{coef_df}")

# Validación cruzada
cv_scores = cross_val_score(svm_model, X, y, cv=5, scoring='accuracy')
print(f'\nPuntajes de precisión en cada fold: {cv_scores}')
print(f'Precisión media: {cv_scores.mean():.2f} ± {cv_scores.std():.2f}')

# Obtener probabilidades para la curva ROC
y_prob_auc = svm_model.predict_proba(x_test)

# Calcular curva ROC y AUC para cada clase
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(label_binarize(y_test, classes=np.unique(y))[:, i], y_prob_auc[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Calcular el AUC promedio (macro)
roc_auc_macro = roc_auc_score(label_binarize(y_test, classes=np.unique(y)), y_prob_auc, multi_class="ovr")

# Crear figura con dos subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Graficar curvas ROC
for i in range(n_classes):
    ax1.plot(fpr[i], tpr[i], 
             label=f'Clase {i} (AUC = {roc_auc[i]:.2f})')

# Añadir línea diagonal de referencia
ax1.plot([0, 1], [0, 1], 'k--', label='Línea de referencia')

# Personalizar gráfico ROC
ax1.set_xlim([0.0, 1.0])
ax1.set_ylim([0.0, 1.05])
ax1.set_xlabel('Tasa de Falsos Positivos')
ax1.set_ylabel('Tasa de Verdaderos Positivos')
ax1.set_title(f'Curva ROC - AUC Macro: {roc_auc_macro:.2f}')
ax1.legend(loc="lower right")
ax1.grid(True, linestyle='--', alpha=0.7)

# Graficar importancia de características
ax2.barh(coef_df.index, coef_df["Importancia"], color="royalblue")
ax2.set_title("Importancias de Características")
ax2.set_xlabel("Importancia")
ax2.set_ylabel("Características")
ax2.grid(axis="x", linestyle='--', alpha=0.7)

# Ajustar layout
plt.tight_layout()
plt.savefig('svm_resultados.png')
plt.show()