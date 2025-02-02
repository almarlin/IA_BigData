import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, label_binarize
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc, roc_auc_score
from imblearn.under_sampling import AllKNN
from imblearn.over_sampling import SMOTE
from sklearn.inspection import permutation_importance



# Cargar el dataset
df = pd.read_csv("Dataset_Academico.csv")

X = df.drop("rendimiento_academico", axis=1)
y = df["rendimiento_academico"]

# Binarizar etiquetas para la curva ROC-AUC
y_bin = label_binarize(y, classes=np.unique(y))
n_classes = y_bin.shape[1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Aplicar AllKNN y Smote para balancear clases
allknn = AllKNN(n_neighbors=3, allow_minority=True)
X_train_reduced, y_train_reduced = allknn.fit_resample(X_train, y_train)

# Aplicamos SMOTE después
smote = SMOTE(random_state=42)
X_train_final, y_train_final = smote.fit_resample(X_train_reduced, y_train_reduced)

# Entrenar modelo
knn_model = KNeighborsClassifier(n_neighbors=3, metric='euclidean', weights='distance')
knn_model.fit(X_train_final, y_train_final)

# Predicción y evaluación
y_pred = knn_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

conf_matrix = confusion_matrix(y_test, y_pred)
print(f'Matriz de confusión: \n{conf_matrix}')
print(np.unique(y))  # Verifica las clases y su orden


report = classification_report(y_test, y_pred)
print(f'Reporte de clasificación:\n{report}')

# Mostrar la Importancia junto con los nombres de las características
# Calcular la importancia por permutación
result = permutation_importance(knn_model, X_test, y_test, n_repeats=10, random_state=42)

# Crear un DataFrame para visualizar los resultados
coef_df = pd.DataFrame({
    'Feature': X.columns,
    'Importancia': result.importances_mean
}).sort_values(by='Importancia', ascending=False)

print(coef_df)


# Validación cruzada
cv_scores = cross_val_score(knn_model, X, y, cv=5, scoring='accuracy')
print(f'Puntajes de precisión en cada fold: {cv_scores}')
print(f'Precisión media: {cv_scores.mean():.2f} ± {cv_scores.std():.2f}')

# Obtener probabilidades para la curva ROC (para cada clase)
y_prob = knn_model.predict_proba(X_test)

# Calcular curva ROC y AUC para cada clase
fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(label_binarize(y_test, classes=np.unique(y))[:, i], y_prob[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Calcular el AUC promedio (macro)
roc_auc_macro = roc_auc_score(label_binarize(y_test, classes=np.unique(y)), y_prob, multi_class="ovr")


fig, diagrama = plt.subplots(2, 1, figsize=(7, 7))

# Graficar curvas ROC en la subfigura [0,0]
for i in range(n_classes):
    diagrama[0].plot(fpr[i], tpr[i], label=f'Clase {i} (AUC = {roc_auc[i]:.2f})')

# Línea diagonal de referencia
diagrama[0].plot([0, 1], [0, 1], 'r--')

# Ajustes del gráfico
diagrama[0].set_xlim([0.0, 1.0])
diagrama[0].set_ylim([0.0, 1.05])
diagrama[0].set_xlabel('False Positive Rate')
diagrama[0].set_ylabel('True Positive Rate')
diagrama[0].set_title(f'Curva ROC - AUC Macro: {roc_auc_macro:.2f}')
diagrama[0].legend(loc="lower right")

# Gráfico de barras horizontales
diagrama[1].barh(coef_df.index, coef_df["Importancia"], color="royalblue")

# Ajustes del gráfico 
diagrama[1].set_title("Importancias de KNN")
diagrama[1].set_xlabel("Importancia")
diagrama[1].set_ylabel("Características")
diagrama[1].grid(axis="x", linestyle="--", alpha=0.7)  # Líneas de referencia en el eje X

plt.tight_layout() 
plt.savefig("knn_resultados.png")
plt.show()


