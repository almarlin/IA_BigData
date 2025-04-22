a <- 100

v <- c(1,3,4)

a
v

is.vector(a)
is.vector(v)

v <- 2*v+1
v

w <- c(8,6,4)

z <- v+w

z[2]

str(z)

sum(is.na(v))                  # núm de valores ausentes
v_ <- c(NA,v,NA,NA) # un vector con tres valores ausentes
v_
sum(is.na(v_))            # núm valores ausentes

quantile(v)

quantile(v, probs =c(0 ,0.1,0.9,1 )) # 80/20
summary(v)

cor(v,w)

sort(w)
sort(v,decreasing = TRUE)

order(w)

v <- c(10,20,30,30,60,50)      # un vector 
w <- c(20,10,31,31,61,51)      # otro vector 
u <- c(5 ,5 ,5 ,32,62,49)      # otro vector

rank(w, ties.method="min")     # vector de rangos mín
# y se usa normalmente para 
# las competiciones deportivas
rank(w, ties.method="max")    # vector de rangos máx
# se usa normalmente para data sciences


pmax(v,w,u)                  # valores máximo miembro a miembro
pmin(v,w,u)                  # valores mínimos miembro a miembro
cumsum(v)                    # sumas acumuladas 
cumprod(v)                   # productos sucesivos
cummax(w)                    # máximo entre miembros considerados y miembros precedentes
cummin(w)                    # ídem con mín



# booleanos - comparaciones#
a <- 1
b <- 2
(a == 1 ) 
(a == b) 
(a <= b)
A <- c(TRUE,TRUE,FALSE,FALSE)
B <- c(TRUE,FALSE,TRUE,FALSE)
A & B     # tabla de verdad de "y"
A | B     # tabla de verdad de "o"
! A       # no-A
xor(A,B)  # tabla de verdad del o exclusivo 
!A|B      # tabla de la implicación A==>B
c <- (a > b)  # almacenar el resultado de una prueba
c

v <- c(10,20,30,30,60,50)      # un vector
t <- (v > 30) # vector resultante de la prueba 
t # miembro a miembro

w <- v[(v>30)]                # solo guardamos los miembros con expresión TRUE
w


which(v == 30) # encontrar los índices para los que el miembro es igual a 30
which(v == 30) # encontrar los índices para los que el miembro es igual a 30
which(v == max(v))# encontrar los índices para los que
# el miembro tiene un valor máximo
which(v == min(v)) # ídem pero buscando mín


nombres <-c(10,12,14)
names(nombres) <-c("Adán","Eva","David")
nombres
nombres["Eva"] #encontrar el valor correspondiente a la clave «Eva»
nombres[nombres[]>10] #extraer las claves cuyo valor es superior a 10


H <- unique(c("e","g","g","h","h","h")) 
H

P <- c("e","f","g","h")
Q <- c("g","h","i","j") 
union(P,Q)
intersect(P,Q)
setdiff(P,Q) #la diferencia no es simétrica
setdiff(Q,P)

union(setdiff(P,Q),setdiff(Q,P)) #diferencia simetrica


H
P
H %in% P 
P %in% H

#para los índices correspondientes:
which(P %in% H)












