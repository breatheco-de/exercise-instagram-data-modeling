# Create the database model for Instagram

**Important**: To do this activity you need to `fork` [this repo](https://github.com/breatheco-de/exercise-instagram-data-modeling) into your **Github** account and then open the forked repo on Gitpod.

Inside he `src/models.py` file you will find a couple of classes describing an example database.

Here is a 4min video explaining what UML is: [https://www.youtube.com/watch?v=UI6lqHOVHic](https://www.youtube.com/watch?v=UI6lqHOVHic)

Th `diagram.png` file generates a database chart based on the classes that you will be creating. Such charts in Database Management are referred to as ERDs (Entity Relatonship Diagrams). 

Please watch these two short videos explaining ERDs: 
[https://www.youtube.com/watch?v=QpdhBUYk7Kk&t=4s](https://www.youtube.com/watch?v=QpdhBUYk7Kk&t=4s)
[https://www.youtube.com/watch?v=-CuY5ADwn24&t=738s](https://www.youtube.com/watch?v=-CuY5ADwn24&t=738s)

You will have to create the Entity Relationship Diagram for Instagram's Database - a very similar diagram to this one:

![Instagram Diagram](https://github.com/breatheco-de/exercise-instagram-data-modeling/blob/master/assets/example.png?raw=true)
[Click to open diagram](https://app.quickdatabasediagrams.com/#/d/LxNXQZ)

> 🔥 You can use this FREE tool to practice your diagram for the first time: https://app.quickdatabasediagrams.com/#/d/


## 💻 Installation

1. Get inside the environment `$ pipenv shell`

2. Install all dependencies `$ pipenv install`

3. Generate the diagram as many times as you need `$ python3 src/models.py`

4. Open the file `diagram.png` to check out your ERD diagram!


## 📝Instructions

Your job is to update the `src/models.py` file with the code needed to replicate Instagram's data model.

The project is using the SQLAlchemy Python library to generate the database.

- What tables do you think instagram might have on its database: E.g: Post, User, etc.?
- What properties should go inside the user? or inside the Post table?
- Please add at least 4 models with all of its properties.
- Refresh the `diagram.png` file at the end by running `$ python3 src/models.py` on the console.


