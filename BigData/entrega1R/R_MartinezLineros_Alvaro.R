##Ejercicios básicos---------------------------------------------

# Calculadora simple
3 + 5 * 2
# 13
10^2
# 100
sqrt(144)
# 12
log(pi)
# 1.14473

# Asignación de variables
# Asigna 100 a a usando <-.
a <- 100
# Imprime a, luego recalcula a <- a + 50 y vuelve a imprimir.
print(a)
a <- a + 50
print(a)
# Vectores numéricos
# Crea v <- c(10, 20, 30, 40, 50) y muestra su longitud con length().
v <- c(10,20,30,40,50)
length(v)
# Multiplica v * 2 y suma 5 a cada elemento.
v <- v*2
print(v)
v <- v+5
print(v)
# Funciones elementales
# 
# Aplica mean(), sum(), min(), max() y sd() a v.

mean(v) # Media
sum(v) # Suma de sus elementos
min(v) # Número menor del vector
max(v) # Número mayor del vector
sd(v) # Desviación estándar del vector

# ¿Qué sucede si insertas un NA en v y vuelves a calcular mean(v)? Prueba luego con mean(v, na.rm = TRUE).
# Devuelve NA. Sin embargo, al hacer na.rm = TRUE eliminamos los NA del vector, pudiendo hacer mean(v) correctamente
v <- c(v,NA)
mean(v)
mean(v,na.rm = TRUE)


# Indexación básica
# 
# Extrae el tercer elemento de v.
v[3]
# Extrae los elementos de la 2ª a la 4ª posición.
v[c(2,4)]
# Operaciones lógicas
# 
# Dado w <- c(5, 15, 25, 35, 45), crea un filtro sel <- w > 20 y aplícalo a w[sel].
w <- c(5, 15, 25, 35, 45)
sel <- w > 20
w[sel]

# Usa which() para obtener los índices donde w == 25. ​
which(w == 25)
# Redondeo
# 
# Redondea pi a 0, 1 y 3 decimales con round().
round(pi,0)
round(pi,1)
round(pi,3)
# Secuencias y repeticiones
# 
# Genera seq(0, 1, by = 0.2) y rep(1:3, each = 4). ​
seq(0, 1, by = 0.2)
rep(1:3, each = 4)
# Uso de paste()
# 
# Junta "Hola" y "mundo" con y sin separador (paste, paste0).
paste("Hola","Mundo",sep = "")
paste("Hola","Mundo",sep = " ")
# Primer histograma
# 
# Para v <- rnorm(100), dibuja hist(v) y observa la distribución.

v <- rnorm(100)

hist(v)
# En este histograma podemos ver una distribución normal

##Ejercicios intermedios---------------------------------------------
# (Manipulación de datos, funciones y estructuras)
# 
# Cuantiles y resumen
# 
# Con tu vector v <- rnorm(200), calcula quantile(v) y summary(v). ¿Qué indican los cuartiles? ​
v <- rnorm(200)
quantile(v) # Distribución en cuartiles
summary(v)  # Resumen del vector, 1er cuartil, mediana, media, 3er cuartil y máximo
# Ordenación y rangos
# 
# Ordena w <- sample(1:20, 10) en orden creciente y decreciente con sort().

w <- sample(10:20,10)
sort(w) # Por defecto es creciente
sort(w,decreasing = TRUE) # Indicamos decreciente

# Obtén el orden de los índices con order() y los rangos con rank() (usa ties.method = "min").
order(w)
rank(w)
rank(w,ties.method = "min") # Los empates se resuelven como el rango mas bajo posible del grupo
# Manejo de NA
# 
# Crea u <- c(NA, 2, NA, 5, 8, NA).
u <- c(NA, 2, NA, 5, 8, NA)
# Cuenta NAs con sum(is.na(u)).

sum(is.na(u))
# Elimina NAs con u[!is.na(u)].
u[!is.na(u)]
# Tablas y frecuencias
# 
# Dado colores <- factor(c("rojo","azul","rojo","verde","azul")), genera table(colores). ​
colores <- factor(c("rojo","azul","rojo","verde","azul"))
print(colores)
table(colores)
# Matrices y apply()
# 
# Construye m <- matrix(1:12, nrow = 3, byrow = TRUE).
m <- matrix(1:12, nrow = 3, byrow = TRUE)
print(m)
# Usa apply(m, 1, sum) y apply(m, 2, mean).
apply(m,1,sum)
apply(m,2,mean)
# Listas
# 
# Crea l <- list(nombre="Ana", edades=c(20,30,40), activo=TRUE).
l <- list(nombre="Ana", edades=c(20,30,40), activo=TRUE)
# Accede a l$nombre y al segundo elemento de l$edades. ​
print(l$nombre)
print(l$edades[2])
# Data frame simple
# 
# Construye df <- data.frame(id=1:5, score=rnorm(5)).
df <- data.frame(id=1:5, score=rnorm(5))
print(df)
# Añade la columna passed <- df$score > 0.
passed <- df$score > 0
# Funciones propias
# 
# Escribe f <- function(x) x^2 + 2*x + 1. Prueba f(5) y usa sapply(1:10, f). ​
f <- function(x) x^2 + 2*x + 1
f(5)
# Control de flujo
# 
# Implementa con for un bucle que calcule los primeros 10 factoriales.
factoriales <- numeric(10)

# Calculamos los factoriales del 1 al 10
for (i in 1:10) {
  fact <- 1
  for (j in 1:i) {
    fact <- fact * j
  }
  factoriales[i] <- fact
}
# Reescribe con while hasta que factorial > 1e5.

# Inicializamos las variables
i <- 1
fact <- 1

# Calculamos los factoriales con el bucle while hasta que el factorial sea mayor que 1e5
while (fact <= 1e5) {
  fact <- fact * i
  cat(i, "!", "=", fact, "\n")  # Mostramos el valor de i! en cada iteración
  i <- i + 1
}

# Factores ordenados
# 
# Crea talla <- factor(c("S","M","L","M","S"), levels=c("S","M","L"), ordered=TRUE).
talla <- factor(c("S","M","L","M","S"), levels=c("S","M","L"), ordered=TRUE)

# Comprueba talla > "M".
print(talla > "M")

### Ejercicios avanzados------------------------------------------------
# 
# (Programación funcional, cadenas, fechas, complejos y OOP)
# 
# tapply() en agrupaciones
# 
# Dado df <- data.frame(grupo=rep(LETTERS[1:3], each=5), valor=rnorm(15)), usa tapply(df$valor, df$grupo, mean).
df <- data.frame(grupo=rep(LETTERS[1:3], each=5), valor=rnorm(15))
tapply(df$valor, df$grupo, mean) # Hace la media para los grupos de valores
# Funciones anónimas
# 
# Aplica sapply(1:5, function(x) ifelse(x%%2==0, "par","impar")).
sapply(1:5, function(x) ifelse(x%%2==0, "par","impar")) # Funcion anonima que determina si un número es par o impar
# Expresiones regulares
# 
# Con text <- "Visita http://example.com y https://r-project.org", elimina URLs usando gsub(). ​
text <- "Visita http://example.com y https://r-project.org"
gsub("https?://[a-zA-Z0-9./?=_-]+", "", text) # Sustituye las urls que encajen en esa expresion regular con ""

# cut() y cuantiles
# 
# Divide 100 valores de rnorm(100) en cuartiles con cut(..., breaks=quantile(...), labels=FALSE).

o <- rnorm(100)
cut(o,breaks=quantile(o,probs=0:4/4),labels=FALSE) # Indica a que cuartil pertenece cada numero del vector
# Fechas y horas
# 
# Convierte "21/04/2025" a Date con as.Date(..., "%d/%m/%Y").
fecha <- as.Date("21/04/2025","%d/%m/%Y")

# Suma 30 días y calcula la diferencia con Sys.Date().
print(fecha + 30)
fecha <- fecha + 30
print (fecha - Sys.Date())
# Complejos y módulo
# 
# Define z <- 3 + 4i. Obtén Mod(z), Arg(z). Dibuja en un plot el punto (Re(z), Im(z)).
z <- 3 + 4i # Se define el numero complejo
print(Mod(z)) # Modulo
print(Arg(z)) # Argumento
plot(Re(z),Im(z)) # Graficamos el punto en el plano complejo
# Pila con RC
# 
# Implementa una clase Stack con Reference Classes que tenga métodos put(), pop() y size(). ​








# Histogramas avanzados
# 
# Ajusta el número de bins en hist() para visualizar rnorm(1000) con distintos parámetros. ​
hist(rnorm(1000),breaks=50) # Con breaks podemos indicar la cantidad de contenedores (bins) a mostrar en el histograma
# Programación vectorizada vs bucles
# 
# Mide con Sys.time() el tiempo de sapply() vs un for para calcular x^3 + x^2 + 1/(x+10) en vectores de hasta 1e6 elementos.







# Crear un vector de valores de x
x <- 1:1e6

# Medir el tiempo usando sapply()
start_time_sapply <- Sys.time()
result_sapply <- sapply(x, function(xi) xi^3 + xi^2 + 1/(xi + 10))
end_time_sapply <- Sys.time()
time_sapply <- end_time_sapply - start_time_sapply
print(paste("Tiempo con sapply():", time_sapply))

# Medir el tiempo usando un bucle for
start_time_for <- Sys.time()
result_for <- numeric(length(x))  # Crear un vector vacío para los resultados
for (i in 1:length(x)) {
  result_for[i] <- x[i]^3 + x[i]^2 + 1/(x[i] + 10)
}
end_time_for <- Sys.time()
time_for <- end_time_for - start_time_for
print(paste("Tiempo con for:", time_for))
# Función de orden superior
# 
# Escribe dualize <- function(f) function(x) f(f(x)) y prueba con sqrt o log. ​
dualize <- function(f) function(x) f(f(x)) 
# Aplica 2 veces la misma funcion

dual_sqrt <- dualize(sqrt)
print(dual_sqrt(16))

dual_log <- dualize(log)
print(dual_log(16))




