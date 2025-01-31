import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder, label_binarize
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc, roc_auc_score
from imblearn.over_sampling import SMOTE

df = pd.read_csv("Dataset_Academico.csv")

x = df.drop("rendimiento_academico",axis=1)
y = df["rendimiento_academico"]

# Seleccionamos el 80% de los datos para entrenar al modelo y el 20% restante servirá para ponerlo a prueba
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(X_train)
x_test = scaler.transform(X_test)

smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(x_train, y_train)

rf_model = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42, class_weight='balanced',min_samples_split=10,min_samples_leaf=10)
rf_model.fit(X_train_smote, y_train_smote)
# rf_model.fit(X_train, y_train)


y_pred = rf_model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

conf_matrix = confusion_matrix(y_test,y_pred)
print(f'Matriz de confusión: \n{conf_matrix}')

report=classification_report(y_test,y_pred)
print(f'Reporte de clasificación:\n{report}')
# Usamos la validación cruzada con 5 "folds"
cv_scores = cross_val_score(rf_model, x, y, cv=5, scoring='accuracy')  # Puedes cambiar 'accuracy' por 'f1_weighted' u otras métricas si lo prefieres

# Imprimimos los resultados
print(f'Puntajes de precisión en cada fold: {cv_scores}')
print(f'Precisión media: {cv_scores.mean():.2f} ± {cv_scores.std():.2f}')




