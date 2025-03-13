<!--hide-->
# Create the database model for Instagram
<!--endhide-->


<onlyfor saas="false" withBanner="false">

## 🌱 How to start this project

**Important**: To do this activity you need to `fork` [this repo](https://github.com/4GeeksAcademy/flask-rest-hello) into your **Github** account and then open the forked repo on [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recommended) or Gitpod.


In the `src/models.py` file of the forked repository, you will find several classes that represent the structure of a sample database.

Here is a 10 min video explaining what UML is: [https://www.youtube.com/watch?v=UI6lqHOVHic](https://www.youtube.com/watch?v=UI6lqHOVHic)

The `diagram.png` file generates a database chart based on the classes that you will be creating. Such charts in Database Management are referred to as ERDs (Entity Relatonship Diagrams). 

Please watch these two short videos explaining ERDs: 
+ [https://www.youtube.com/watch?v=QpdhBUYk7Kk](https://www.youtube.com/watch?v=QpdhBUYk7Kk)
+ [https://www.youtube.com/watch?v=-CuY5ADwn24](https://www.youtube.com/watch?v=-CuY5ADwn24)

</onlyfor>

You will have to create the Entity Relationship Diagram for Instagram's Database - a very similar diagram to this one:

![Instagram Diagram](https://github.com/breatheco-de/exercise-instagram-data-modeling/blob/master/assets/example.png?raw=true)
[Click to open diagram](https://app.quickdatabasediagrams.com/#/d/LxNXQZ)

> 🔥 You can use this FREE tool to practice your diagram for the first time: https://app.quickdatabasediagrams.com/#/d/


## 💻 Installation

1. Get inside the environment `$ pipenv shell`

2. Install all dependencies `$ pipenv install`

3. To generate a database diagram as many times as needed, run `$ pipenv run diagram`

4. Once the `diagram.png` file is created in the root of the project, open it to see the UML representation of your database.


## 📝Instructions

Your job is to update the `src/models.py` file with the code needed to replicate Instagram's data model.

The project is using the SQLAlchemy Python library to generate the database.

- What tables do you think Instagram might have on its database: E.g: Post, User, etc.?
- What properties should go inside the User? or inside the Post table?
- Please add at least 4 models with all of their properties.
- Refresh the `diagram.png` file at the end by running `$ python src/models.py` on the console.

This and many other projects are built by students as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).

