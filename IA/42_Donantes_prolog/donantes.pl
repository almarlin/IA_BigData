% Estructuras

% Hechos: donante(persona(Nombre, Apellido1, Apellido2), Grupo, Rh).
donante(persona(juan, campos, ruiz), a, positivo).
donante(persona(ana, lara, silva), ab, negativo).
donante(persona(luis, luna, pachecho), ab, negativo).
donante(persona(alvaro, perez, garcia), o, negativo).
donante(persona(carla, merida, frutos), o, positivo).
donante(persona(lucia, luna, pachecho), ab, positivo).
donante(persona(pepito, de_los, palotes), ab, positivo).


% Compatibilidad de grupo sanguíneo y factor RH

puede_donar_a(Donante, Receptor) :-
    donante(Donante, GrupoD, RhD),
    donante(Receptor, GrupoR, RhR),
    compatible(GrupoD, GrupoR),
    compatible_rh(RhD, RhR).

% Compatibilidad de grupos sanguíneos
compatible(o, _).
compatible(a, a).
compatible(a, ab).
compatible(b, b).
compatible(b, ab).
compatible(ab, ab).

% Compatibilidad de factor Rh
compatible_rh(negativo, negativo).
compatible_rh(negativo, positivo).
compatible_rh(positivo, positivo).

contar_por_grupo_y_factor(Grupo, Rh, N) :-
    findall(1, donante(_, Grupo, Rh), Lista),
    length(Lista, N).


guardar_donantes :-
    write('Grupo sanguineo (o, a, b, ab): '), read(Grupo),
    write('Factor RH (positivo, negativo): '), read(Rh),
    write('Nombre del fichero entre comillas dobles (ej. "donantes.txt"): '), read(NombreFichero),
    open(NombreFichero, write, Stream),
    forall(
        donante(persona(N, A1, A2), Grupo, Rh),
        (
            format(Stream, '~w ~w ~w~n', [N, A1, A2])
        )
    ),
    close(Stream),
    write('Archivo generado con éxito.'), nl.
