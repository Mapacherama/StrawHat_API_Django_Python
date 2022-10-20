# StrawHat API. Made possible with GraphQL, SQLAlchemy, Flask & Python

![](https://upload.wikimedia.org/wikipedia/en/thumb/2/2c/One_Piece_Logo.svg/800px-One_Piece_Logo.svg.png)

My favorite thing in the world is sitting in my pajama's and watching One Piece on Sunday morning.
That's why I decided to make this API, to gain more knowledge about programming in Python and also 
gain more knowledge about the incredible world Oda has created!

## Diagram of the project

![](https://raw.githubusercontent.com/Mapacherama/StrawHat_API_GraphQL_Python/main/Diagrams/PirateClassDiagram.png)


## Technologies used

- Flask
- SQLAlchemy
- Ariadne
- Pytest

## Good to know

## Step 1: Getting started

Create a virtual environment using virtualenv or conda and then run the command ` pip install -r requirements.txt` or ` pip3 install -r requirements.txt ` to install the dependencies.

Make sure to run the activate file in the environment



# Run Graphql playground

Execute the command ` cd StrawhatAPI ` and after that  ` flask run ` remember to be in the directory where your app.py is or the point
input of your application. visit `http://localhost:5000/graphql `. In the [GraphQL playground](https://github.com/graphql/graphql-playground/releases/tag/v1.8.10) of choice (I prefer the client myself).

# Simple query example
```GraphQL
query{
  getSingleCharacter(id:"1"){
    character{
      name
      nickName
    }
  }
}
```


