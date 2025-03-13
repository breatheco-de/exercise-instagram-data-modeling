<!--hide-->
# Crea el modelo de base de datos para Instagram
<!--endhide-->


<onlyfor saas="false" withBanner="false">

## 🌱 Cómo iniciar este proyecto

**Importante**: Para realizar esta actividad necesitas hacer un `fork` de [este repo](https://github.com/4GeeksAcademy/flask-rest-hello) en tu cuenta de **Github** y luego abrir el *fork* en [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recomendado) o Gitpod.

En el archivo `src/models.py` del repositorio forkeado, encontrarás varias clases que representan la estructura de una base de datos de ejemplo

Aquí hay un video de 10 minutos que explica qué es UML: [https://www.youtube.com/watch?v=UI6lqHOVHic](https://www.youtube.com/watch?v=UI6lqHOVHic)

</onlyfor>

Vamos a crear el Diagrama de relación de entidad para la base de datos de Instagram, un diagrama muy similar a este:

![Diagrama de Instagram](https://github.com/breatheco-de/exercise-instagram-data-modeling/blob/master/assets/example.png?raw=true)
[Clic para abrir el diagrama](https://app.quickdatabasediagrams.com/#/d/LxNXQZ)

> 🔥 Puedes usar esta herramienta GRATUITA para practicar tu diagrama por primera vez: https://app.quickdatabasediagrams.com/#/d/

## 💻 Instalación

1. Entra dentro del environment (entorno) `$ pipenv shell`

2. Instala todas las dependencias `$ pipenv install`

3. Para generar un diagrama de la base de datos tantas veces como sea necesario `$ pipenv run diagram`

4. Una vez creado el archivo `diagram.png` en la raiz del proyecto, abrelo para ver la representación UML de tu base de datos.

## 📝 Instrucciones

Tu trabajo es actualizar el archivo `src/models.py` con el código necesario para replicar el modelo de datos de Instagram.

El proyecto está utilizando la librería Python SQLAlchemy para generar la base de datos.

- ¿Qué tablas crees que Instagram podría tener en su base de datos, por ejemplo: Post, Usuario, etc.?
- ¿Qué propiedades deben ir dentro de la tabla Usuario? o ¿Dentro de la tabla Post?
- Agrega al menos 4 modelos con todas sus propiedades.
- Actualiza el archivo `diagram.png` al final ejecutando `$ python src/models.py` en la consola.

Este y otros proyectos son usados para [aprender a programar](https://4geeksacademy.com/es/aprender-a-programar/aprender-a-programar-desde-cero) por parte de los alumnos de 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) realizado por [Alejandro Sánchez](https://twitter.com/alesanchezr) y muchos otros contribuyentes. Conoce más sobre nuestros [Cursos de Programación](https://4geeksacademy.com/es/curso-de-programacion-desde-cero?lang=es) para convertirte en [Full Stack Developer](https://4geeksacademy.com/es/coding-bootcamps/desarrollador-full-stack/?lang=es), o nuestro [Data Science Bootcamp](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning).
