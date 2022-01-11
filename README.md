<p align="center">
  <img src="https://assets.breatheco.de/apis/img/images.php?blob&random&cat=icon&tags=4geeks,128">
  <h4 align="center">4Geeks Academy</h4>
</p>

<p>
    <h2 align="center" style="margin: 0">Instagram data model</h2>
    <h3 align="center" style="margin-top: 0">Ovidio Santoro</h3>
</p>

## Project Description

This is a mock-up database structure for an Instagram-like app.

#### User Table
The `User` table stores three main pieces of data: an `username`, that must be unique (not two users can have the same username), an `email` (equally unique for the same reasons) and a `password` (that should NEVER be stored in plaintext; a hashing algorithm should be used beforehand). In addition to this, the `User` table establishes two relational columns: one to track every `Post` of the user and another to track the `Followers`.

#### Post Table
The `Post` table simply stores a `title` for the post, an `image` address, the `user.id` of the creator and a `description` of the post. Additionaly, it establishes a relationship with the `Comment` table to track each comment the post recieves.

#### Comment Table
The `Comment` table simply stores a `comment` and the id of the user commenting and the post commented.

#### Follower Table
The `Follower` table stores foreign keys to the username of an `User` who is following someone and another `User` that is beign followed.

## Technologies

* SQLAlchemy
* Flask
* Python

## Usage

1. Get inside the environment `$ pipenv shell`
2. Install all dependencies `$ pipenv install`
3. Generate de diagram as many times as you need `$ python src/models.py`
4. Open the file `diagram.png` to check out your UML diagram!

## Contribute / Report Issues

https://github.com/OvidioSantoro/exercise-instagram-data-modeling