from sklearn.metrics import accuracy_score
import cudf
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

categories = ['sci.sapce', 'rec.sport.baseball','talk.politics.guns']
news = fetch_20newsgroups(subset='all',categories=categories,remove=('headers','footers','quotes'))
textos = news.data[:1000]
etiquetas = news.target[:1000]

df = cudf.Dataframe({'texto':textos,'categoria':etiquetas})

df['texto'] = df['texto'].str.replace('[^\w\s]','',regex=True)
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df["texto"])
y = df['categoria'].values

X_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train,y_train)


y_pred = modelo.predict(x_test)
precision = accuracy_score(y_test,y_pred)
print(f"Accuracy: {precision:.4f}")