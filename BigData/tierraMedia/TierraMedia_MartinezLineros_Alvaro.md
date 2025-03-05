# **Calidad de los datos.**

#### Big data aplicado.
#### Alumno: **Álvaro Martínez Lineros**
\# Ejercicio: Calidad de los datos en la Tierra Media

\# Identifica los problemas de calidad en el dataset

\# Aplica las técnicas de limpieza de datos para corregir los problemas:
- Valores faltantes.
- Inconsistencias y errores tipográficos.
- Valores atípicos.
- Errores de formato.
- Reglas de negocio.

# **Valores faltantes.**
Para el tratamiento de los valores faltantes se ha optado por eliminar esos registros.
```python
# Registros con valores nulos:
   ID_Batalla          Nombre_Batalla       Fecha        Lugar                 Bando Líder  Bajas_Enemigas  Bajas_Propias Victoria      Anotaciones
4           5  Batalla de Cuernavilla  3019-03-03  Cuernavilla  Comunidad del Anillo   NaN            8000            NaN       Sí  Defensa exitosa
5           6   Batalla de Lothlórien  3019-03-22   Lothlórien                Saurón   NaN            2000         5000.0       No  Ataque repelido
```
# **Inconsistencias y errores tipográficos.**
Se ha optado por normalizar los nombres de lideres, batallas y bandos. Se han eliminado puntuaciones y acentos. Ejemplo:
```python
# Poner en minuscula
df["Nombre_Batalla"] = df["Nombre_Batalla"].str.lower()
# Eliminar acentos
df["Nombre_Batalla"] = df["Nombre_Batalla"].apply(lambda x: unidecode(str(x)) if isinstance(x, str) else x)
# Eliminar puntuaciones
df["Nombre_Batalla"] = df["Nombre_Batalla"].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", str(x)))
```
# **Valores atípicos**
Los valores atípicos no han sido modificados ni eliminados. Sin embargo los valores negativos han sido cambiados a positivos.
```python
# Modificacion de datos inválidos
df["Bajas_Enemigas"] = df["Bajas_Enemigas"].apply(lambda bajas: bajas * -1 if bajas < 0 else bajas)
```
# **Errores de formato**
Las fechas presentaban un error de formato. Todas han sido normalizadas a %Y-$m-%d.
```python
# Cambio de formato de fecha
df["Fecha"] = df["Fecha"].apply(lambda fecha: parser.parse(fecha))
df["Fecha"] = df["Fecha"].apply(lambda fecha: datetime.strftime(fecha, "%Y-%m-%d"))
```
# **Reglas de negocio**
Se presentaba inconsistencia en la determinación de una victoria y a través de sus anotaciones se pudo intuir que se trataba de una derrota.
```python
print(f"Resultados mal guardados\n{df[df['Victoria'].apply(lambda victoria: victoria not in ('Sí', 'No', 'Empate'))]}\n")
# En este caso al tener las anotaciones podemos ver que se repelió el ataque, por lo tanto vamos a considerarlo una derrota
df["Victoria"] = df['Victoria'].apply(lambda victoria: "No" if victoria not in ('Sí', 'No', 'Empate') else victoria)

```
# **Conclusiones.**
Después de esta normalización los datos presentan una buena consistencia y un buen formato para ser manipulados o estudiados.