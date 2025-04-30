% --------- Datos ---------
% Definimos los hechos de padre y madre. 

:- discontiguous padre/2.
:- discontiguous madre/2.

% padre(Padre, Hijo)
% madre(Madre, Hijo)

% Nivel 0: inicio
padre(hermenegildo,carlos).
madre(lucrecia,carlos).

padre(hermenegildo,juan).
madre(lucrecia,juan).

padre(hermenegildo,isabel).
madre(lucrecia,isabel).

% Nivel 1: abuelos
padre(carlos, alejandro).    % alejandro es hijo de carlos
madre(maria, alejandro).    % alejandro es hijo de maria

padre(juan, beatriz).       % beatriz es hija de juan
madre(elena, beatriz).      % beatriz es hija de elena

padre(luis, antonio).       % antonio es hijo de luis
madre(isabel, antonio).     % antonio es hijo de isabel

% Nivel 2: padres (hijos de los abuelos)

padre(alejandro,lucia).
madre(laura,lucia).
padre(alejandro,juanito).
madre(laura,juanito).

padre(manuel,ana).
madre(beatriz,ana).
padre(manuel, pedro).      
madre(beatriz, pedro).

padre(antonio,alvaro).
madre(antonia,alvaro).
padre(antonio, clara).       
madre(antonia, clara).

% Nivel 3: hijos (nietos de los abuelos)

padre(tomas,luna).
madre(lucia,luna).
padre(tomas, rosa).
madre(lucia, rosa).     

padre(juanito,cristina).
madre(alba,cristina).

padre(lucas,valeria).
madre(ana,valeria).

padre(alvaro,diego).
madre(helena,diego).
padre(alvaro, emilia).   
madre(helena, emilia).   

% Nivel 4: bisnietos (hijos de los nietos)

padre(mateo,sofia).
madre(luna,sofia).

padre(carlo,aitana).
madre(valeria,aitana).
padre(carlo, bea).       
madre(valeria, bea).      

padre(diego,javier).
madre(marina,javier).
padre(diego, samuel).     
madre(marina, samuel).    

% Nivel 5: tataranietos (hijos de los bisnietos)

padre(ricardo,camila).
madre(sofia,camila).
padre(ricardo, simon).         
madre(sofia, simon).      

padre(fernando,valentina).
madre(aitana,valentina).
padre(fernando, sergio).   
madre(aitana, sergio).       

padre(javier,andres).
madre("maria isabel",andres).

padre(samuel,nico).
madre(teresa,nico).

% --------- Reglas ---------

% ; or
% , and

% hermano(X, Y): si X e Y comparten padre o madre
hermano(X, Y) :- 
    (padre(P,X), padre(P,Y), X \= Y);  % Si comparten el mismo padre
    (madre(M,X), madre(M,Y), X \= Y).  % Si comparten la misma madre

% abuelo(X, Y): si X es el abuelo de Y
abuelo(X, Y) :- 
    (padre(P, Y); madre(P, Y)),  % P es el padre o M es la madre de Y
    (padre(X, P); madre(X, P)),  % X es el padre de P o la madre de M, por lo tanto X es abuelo de Y
    X \= Y.  % Aseguramos que X no es Y (para evitar que X sea el abuelo de sí mismo)

% hijo(X,Y): si X es el hijo de Y
hijo(X,Y) :- 
    padre(Y,X); madre(Y,X).

% nieto(X,Y): si X es el nieto de Y
nieto(X,Y) :- 
    (padre(Y, H); madre(Y, H)),  % Y es el padre o la madre de H
    (padre(H, X); madre(H, X)).  % H es el padre o la madre de X

% bisnieto(X,Y): si X es el bisnieto de Y
bisnieto(X,Y) :- 
    nieto(X,A),  % X es el nieto de A
    (padre(Y, A); madre(Y, A)).  % Y es el padre o madre de A

% tio(X,Y): si X es el tio de Y
tio(X,Y) :-
    hermano(X,P),  % X es hermano de P
    (padre(P,Y); madre(P,Y)),  % P es el padre o la madre de Y
    X \= Y.  % Aseguramos que X no sea Y

% Consultar los hermanos sin duplicados
hermanos_de(Y, Hermanos) :-
    setof(X, hermano(X, Y), Hermanos).  % Genera una lista de hermanos sin duplicados

% Consultar los abuelos sin duplicados
abuelos_de(Y, Abuelos) :-
    setof(X, abuelo(X, Y), Abuelos).  % Genera una lista de abuelos sin duplicados

% Consultar los hijos sin duplicados
hijos_de(Y, Hijos) :-
    setof(X, hijo(X, Y), Hijos).  % Genera una lista de hijos sin duplicados

% Consultar los nietos sin duplicados
nietos_de(Y, Nietos) :-
    setof(X, nieto(X, Y), Nietos).  % Genera una lista de nietos sin duplicados

% Consultar los bisnietos sin duplicados
bisnietos_de(Y, Bisnietos) :-
    setof(X, bisnieto(X, Y), Bisnietos).  % Genera una lista de bisnietos sin duplicados

% Consultar los tíos sin duplicados
tios_de(Y, Tios) :-
    setof(X, tio(X, Y), Tios).  % Genera una lista de tios sin duplicados

% primo(X,Y): si X es el primo de Y
primo(X, Y) :-
    (padre(PX, X); madre(PX, X)),
    (padre(PY, Y); madre(PY, Y)),
    hermano(PX, PY),
    X \= Y.
	


















