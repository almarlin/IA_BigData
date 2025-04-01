### BlockChain telefono.
###### Programación de Inteligencia Artificial (PIA)
###### Álvaro Martínez Lineros 


#### ¿Por qué se usa un hash en cada bloque del blockchain?
Se usa un hash para mantener la veracidad e integridad de la información. Si el contenido es alterado, el hash lo refleja cambiando también.
#### ¿Qué papel cumple el hash_anterior en la integridad de la cadena?
Sirve para comprobar si el bloque ha sido modificado. Al comparar el hash del bloque con el hash_anterior del bloque siguiente se puede verificar que se ha modificado la cadena y que la integridad de los datos está comprometida.
#### ¿Qué similitudes hay entre el juego del teléfono escacharrado y esta simulación?
Se simula una modificación irregular de los datos y posteriormente se validan todos sin comprobar si esos son los primeros datos que crearon los bloques.
#### ¿Se puede “arreglar” la cadena alterando todos los hashes? ¿Por qué eso no es viable en blockchains reales?
Si, en este caso es lo que ocurre en el método "reparar" de la clase Blockchain, sin embargo, esto no es aplicable a un BlockChain real. Esto es porque se debe verificar que el contenido no ha sido modificado, se debe recuperar de una copia de seguridad. En caso de querer modificarlo para tapar o encubrir una actividad maliciosa, no sería efectivo pues al ser un sistema descentralizado, otras cadenas detectarían que la modificada no se corresponde. 