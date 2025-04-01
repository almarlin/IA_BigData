### BlockChain basico.
###### Programación de Inteligencia Artificial (PIA)
###### Álvaro Martínez Lineros 

#### ¿Qué es el hash de un bloque? ¿Por qué es importante que sea único?
El hash de un bloque es el valor resultante de la encriptación de los datos que contiene. Bitcoin usa sha256 para encriptar dichos datos.

La importancia de que este hash sea único radica en:
- *Mantener la integridad de los datos.* El hash verifica que los datos no se hayan modificado.
- *Continuidad de la cadena.* Cada bloque contiene el hash anterior, por lo que cualquier cambio repercutirá en los bloques posteriores. 
- *Prueba de trabajo.* En las actividades de minería de criptomonedas los mineros deben encontrar un hash que cumpla con ciertos requisitos. Esto se conoce como "prueba de trabajo" y es una forma de asegurar que los bloques sean agregados de manera consensuada y que el sistema sea seguro y descentralizado.
- *Identificación única.* Así se facilita el reconocimiento del bloque y la validación de su información.
#### ¿Qué ocurre si se modifica un bloque anterior en la cadena?
Si se modifica un bloque anterior, los siguientes no se corresponderían con el hash ya generado. Además, como cada bloque contiene el hash del bloque anterior, habría que modificar estos también para corregir ese fallo. Aun así, la red descentralizada detectaría que esta red modificada no es válida gracias a otras copias de la misma.
#### ¿Qué representa el bloque génesis y qué lo diferencia de los demás?
El bloque génesis representa el primer bloque de una cadena, es sobre el que se construye el resto. Representa el inicio y el punto de referencia de toda la cadena.

Sus principales diferencias son:
- *No tiene bloque anterior.* Es el único bloque que no hace referencia a un bloque anterior, por lo tanto su referencia está vacía o con un valor predeterminado determinado por los desarrolladores.
- *Su hash es único.* El hash del bloque génesis no es dependiente de otro bloque, este valor suele estar predefinido o generado por un protocolo de la blockchain.
- *Es preconfigurado.* Es un bloque preconfigurado por los desarrolladores del protocolo y no se mina de la misma forma que el resto de bloques.
