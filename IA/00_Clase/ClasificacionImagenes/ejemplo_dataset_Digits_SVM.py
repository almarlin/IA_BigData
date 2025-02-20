from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits

# Cargar el dataset
digits = load_digits()

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Crear y entrenar el modelo SVM
svm_model = SVC(kernel="linear")
svm_model.fit(X_train, y_train)

# Hacer predicciones
y_pred = svm_model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo SVM: {accuracy:.2f}")
