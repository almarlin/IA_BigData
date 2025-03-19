# Es necesario tener instalado WSL en sistemas operativos Windows. Posteriormente, se necesita instalar Ubuntu desde la microsoft store.
# En la consola de Ubuntu, instalar CONDA:
# $ curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
# $ bash Miniforge3-$(uname)-$(uname -m).sh
# Comprobar que el channel_priority sea flexible y si no, cambiarlo:
# $ conda config --show channel_priority
# $ conda config --set channel_priority flexible

# Instalar Rapids con el selector de la ruta: https://docs.rapids.ai/install/#selector 
# Elegir la configuración deseada y ejecutar el código proporcionado en una consola nueva de ubuntu.
# Finalmente, probar la instalacion con un fichero python de la siguiente forma:

# import cudf
# print(cudf.Series([1,2,3])

# El fichero debe ejecutarse desde la consola de ubuntu con Rapids funcionando.
# Para iniciar el entorno con rapids se pueden ejecutar los siguientes comandos:

# $conda env list
# # conda environments:
# #
# base                 * /home/usuario/miniforge3
# rapids-25.02           /home/usuario/miniforge3/envs/rapids-25.02 //Nos quedamos con la versión de rapids.

# $ conda activate rapids-25.02 // Activamos el entorno de rapids.
# $ code . // Abrimos VS Code con el entorno de rapids



from sklearn.metrics import accuracy_score
import cudf
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

categories = ['sci.space', 'rec.sport.baseball','talk.politics.guns']
news = fetch_20newsgroups(subset='all',categories=categories,remove=('headers','footers','quotes'))
textos = news.data[:1000]
etiquetas = news.target[:1000]

df = cudf.DataFrame({'texto':textos,'categoria':etiquetas})

df['texto'] = df['texto'].str.replace('[^\w\s]','',regex=True)

# Cambiar a pandas para poder utilizar TfidVectorizer
texto_pandas = df['texto'].to_pandas()

tfidf = TfidfVectorizer()
X = tfidf.fit_transform(texto_pandas)
y = df['categoria'].values

#  Cambiar a tipos de CUDF a numpy y pandas 
X = X.toarray()
y = y.get()

X_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train,y_train)


y_pred = modelo.predict(x_test)
precision = accuracy_score(y_test,y_pred)
print(f"Accuracy: {precision:.4f}")