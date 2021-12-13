# Crea el modelo de base de datos para Instagram

**Importante**: Para realizar esta actividad necesitas hacer un `fork` de este repo en tu cuenta de **Github** y luego, abrir el *fork* en Gitpod.

Dentro del archivo `src/models.py` encontrarás un par de clases que describen una base de datos de ejemplo.

Aquí hay un video de 4 minutos que explica qué es UML: [https://www.youtube.com/watch?v=UI6lqHOVHic](https://www.youtube.com/watch?v=UI6lqHOVHic)

Vamos a crear el Diagrama de relación de entidad para la base de datos de Instagram, un diagrama muy similar a este:

![Diagrama de Instagram](https://github.com/breatheco-de/exercise-instagram-data-modeling/blob/master/assets/example.png?raw=true)
[Click para abrir el diagrama](https://app.quickdatabasediagrams.com/#/d/LxNXQZ)

> 🔥 Puedes usar esta herramienta GRATUITA para practicar su diagrama por primera vez: https://app.quickdatabasediagrams.com/#/d/


## 💻 Instalación

1. Entra dentro del environment (ambiente) `$ pipenv shell`

2. Instala todas las dependencias `$ pipenv install`

3. Genera el diagrama tantas veces como sea necesario `$ python src/models.py`

4. Abre el archivo `diagram.png` para ver tu diagrama UML!


## 📝Instrucciones

Tu trabajo es actualizar el archivo `src / models.py` con el código necesario para replicar el modelo de datos de instagram.

El proyecto está utilizando la libreria Python SQLAlchemy para generar la base de datos.

- ¿Qué tablas crees que Instagram podría tener en su base de datos: por ejemplo: Publicar, Usuario, etc.?
- ¿Qué propiedades deben ir dentro del usuario? o dentro de la tabla de correos?
- Agrega al menos 4 modelos con todas sus propiedades.
- Regenera el archivo diagram.png al final ejecutando `$ python3 models.py` en la consola.
