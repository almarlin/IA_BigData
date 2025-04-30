% --- Definición de carreteras: carretera(Origen, Destino, Distancia_km).
carretera(algeciras, la_linea_de_la_concepcion, 22).
carretera(algeciras, cadiz, 107).
carretera(algeciras, jerez_de_la_frontera, 125).
carretera(algeciras, malaga, 135).

carretera(almeria, el_ejido, 31).
carretera(almeria, roquetas_de_mar, 26).
carretera(almeria, motril, 108).
carretera(almeria, granada, 166).

carretera(cadiz, jerez_de_la_frontera, 34).
carretera(cadiz, chiclana_de_la_frontera, 26).
carretera(cadiz, san_fernando, 13).
carretera(cadiz, sanlucar_de_barrameda, 60).

carretera(chiclana_de_la_frontera, san_fernando, 12).
carretera(chiclana_de_la_frontera, jerez_de_la_frontera, 30).

carretera(cordoba, sevilla, 140).
carretera(cordoba, jaen, 110).
carretera(cordoba, linares, 120).
carretera(cordoba, granada, 166).

carretera(dos_hermanas, sevilla, 15).
carretera(dos_hermanas, utrera, 21).

carretera(el_ejido, roquetas_de_mar, 15).

carretera(granada, motril, 68).
carretera(granada, jaen, 100).
carretera(granada, malaga, 125).
carretera(granada, cordoba, 166).

carretera(huelva, sevilla, 95).
carretera(huelva, cadiz, 150).

carretera(jaen, linares, 32).

carretera(jerez_de_la_frontera, sanlucar_de_barrameda, 25).

carretera(la_linea_de_la_concepcion, marbella, 74).

carretera(linares, granada, 130).

carretera(malaga, marbella, 58).
carretera(malaga, mijas, 33).
carretera(malaga, velez_malaga, 37).
carretera(malaga, motril, 110).

carretera(marbella, mijas, 35).

carretera(mijas, velez_malaga, 45).

carretera(motril, velez_malaga, 90).

carretera(roquetas_de_mar, el_ejido, 15).

carretera(san_fernando, jerez_de_la_frontera, 35).

carretera(sevilla, utrera, 35).
carretera(sevilla, jerez_de_la_frontera, 92).
carretera(sevilla, malaga, 205).
carretera(sevilla, granada, 256).



% --- Reglas para encontrar rutas entre municipios

ruta(Inicio, Fin, Ruta, Distancia) :-
    ruta(Inicio, Fin, [Inicio], RutaInvertida, 0, Distancia),
    reverse(RutaInvertida, Ruta).

ruta(Fin, Fin, Ruta, Ruta, Dist, Dist).
ruta(Inicio, Fin, Visitados, RutaFinal, DistAcumulada, DistanciaTotal) :-
    carretera(Inicio, Intermedio, Distancia),
    \+ member(Intermedio, Visitados),
    DistNueva is DistAcumulada + Distancia,
    ruta(Intermedio, Fin, [Intermedio|Visitados], RutaFinal, DistNueva, DistanciaTotal).


