from flask import Flask, render_template, request
from blueprint import blueprint
from __init__ import app
import requests
import json

# import app_crud (database stuff)
from crud.app_crud import app_crud

# create a Flask instance

app.register_blueprint(blueprint)
app.register_blueprint(app_crud)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/searchbar/')
def search():
    return render_template("search.html")


@app.route('/F1Schedule/')
def F1Schedule():
    return render_template("F1Schedule.html")

@app.route('/FPCStarWars/')
def FPCStarWars():
    return render_template("FPCStarWars.html")

@app.route('/FPCToyStory/')
def FPCToyStory():
    return render_template("FPCToyStory.html")

@app.route('/FPCPokemon/')
def FPCPokemon():
    return render_template("FPCPokemon.html")

@app.route('/CollectablesGame/')
def CollectablesGame():
    return render_template("CollectablesGame.html")

@app.route('/Pokedex/')
def Pokedex():
    return render_template("Pokedex.html")

@app.route('/PokemonBattle/')
def PokemonBattle():
    return render_template("PokemonBattle.html")

@app.route('/Random/')
def Random():
    return render_template("Random.html")


@app.route('/pokemoncards/')
def pokemon_cards():
    url = "https://pokemon-tcg-card-prices.p.rapidapi.com/card"

    querystring = {"setId":"33ee55f4-30d0-4900-850f-36a351fb9719","set":"vivid-voltage","series":"sword-and-shield"}

    headers = {
        'x-rapidapi-host': "pokemon-tcg-card-prices.p.rapidapi.com",
        'x-rapidapi-key': "7815f70232mshea0c87cc336b4aap13f459jsn464272722115"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    print(data)
    return render_template("pokemon_cards.html", output=data)

@app.route('/pokemongo/')
def pokemon_go():
    url = "https://pokemon-go1.p.rapidapi.com/pokemon_evolutions.json"

    headers = {
        'x-rapidapi-host': "pokemon-go1.p.rapidapi.com",
        'x-rapidapi-key': "9e4650470emshc2461cc01c07b29p18b9b5jsnfa759ab87fca"
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    print(data)
    return render_template("pokemongo.html", output=data)

@app.route('/fortnite/')
def sports_cards():
    return render_template("fortnite.html")


@app.route('/tictactoe/')
def tictactoe():
    return render_template("tictactoe.html")

@app.route('/recommendations/')
def recommendations():
    topic = [
        {"topic": "/static/assets/LGcreatetask/animebutton.PNG", "file": "/subcategories1/"},
        {"topic": "/static/assets/LGcreatetask/fortnitebutton.PNG", "file": "/subcategories2/"},
        {"topic": "/static/assets/LGcreatetask/marvelbutton.PNG", "file": "/subcategories3/"},
        {"topic": "/static/assets/LGcreatetask/starwarsbutton.PNG", "file": "/subcategories4/"},
    ]
    return render_template("LGcreatetask/recommendations.html", topic=topic)

@app.route('/subcategories1/')
def subcategories1():
    return render_template("LGcreatetask/subcategories1.html")


@app.route('/subcategories5/')
def subcategories5():
    return render_template("LCcreatetask/subcategories5.html")


@app.route('/subcategories2/')
def subcategories2():
    return render_template("LGcreatetask/subcategories2.html")


@app.route('/subcategories3/')
def subcategories3():
    return render_template("LGcreatetask/subcategories3.html")


@app.route('/subcategories4/')
def subcategories4():
    return render_template("LGcreatetask/subcategories4.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)