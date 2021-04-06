# Homeria Prueba Tecnica

A continuación se expone una prueba de código a realizar en Python 
en la que se trabajará con un JSON sobre el cuál se harán diferentes operaciones:
- 1 Obtener el JSON de un bucket de S3 mediante un cliente de boto3. El Bucket tiene activo el acceso público y anónimo, 
  por lo que no se necesitan credenciales. El nombre del Bucket es homeria-coding-interview y se debe obtener 
  el JSON cuyo nombre comienza por homeria.
  
- Partiendo del JSON obtenido, generar un nuevo diccionario con las categorías y los productos ordenados por el atributo orden 
  y volcarlo a un fichero.
  
- Partiendo del JSON obtenido, generar un nuevo diccionario sólo con las categorías pero éstas ordenadas alfabéticamente por 
  el atributo nombre y volcarlo a un fichero.
  
- Mostrar un mensaje por pantalla con el nombre y el id de todos aquellos productos que sólo sean subproductos. (Consideramos 
  un producto como sólo subproducto cuando no aparece en una categoría, es decir, sólo está contenido en productos padre).
  
- Mostrar por pantalla el nombre y el identificador de los productos (y sus subproductos, si los hubiera) que pertenecen a la 
  categoría Menús ordenados por el atributo orden.
  
- Calcular la profundidad del elemento o elementos más internos del JSON (siendo la profundidad del objeto padre 0).
  
- Generar un fichero JSON con la frecuencia de aparición de los productos en categorías y/o otros productos. Las claves de 
  este JSON deben ser el nombre de los productos. Por ejemplo, si el producto con nombre X aparece en otro producto Y y la 
  categoría Z, el resultado debería ser:
  
        {
            "X": 2
        }

- Se valorará la dockerización de la prueba, por lo que si se hace uso de Docker, adjuntar el fichero Dockerfile

## Ejecución del proyecto

```shell
pipenv run python app/main.py
```

## Ejecución con Docker

```shell 
docker-compose up
```
