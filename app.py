from flask import Flask, render_template

app = Flask(__name__)

# Sample Game Data
GAMES = [
    {
        "id": "bunny-rage",
        "title": "ShooterBunnyRageGame",
        "category": "Platformer / Shooter",
        "description": "It's a bunny. It's a shooter. It's a RAGE GAME???",
        "image": "https://picsum.photos/id/1060/600/400",
        "game_url": "https://programexy.github.io/Shooter-bunny-rage-game/" # Sample HTML5 game
    },
    {
        "id": "aoti",
        "title": "Attack of the Insects",
        "category": "Platformer / Shooter",
        "description": "I know you loved the ShooterBunnyRageGame. Here is the sequel. (don't worry it's not a rage game)",
        "image": "https://picsum.photos/id/1015/600/400",
        "game_url": "https://programexy.github.io/aoti"
    },
    {
        "id": "monking",
        "title": "whoops cant tell u about this one yet",
        "category": "Platformer / Adventure",
        "description": "Wowzers. Lions????",
        "image": "https://picsum.photos/id/1059/600/400",
        "game_url": "womp womp"
    }
]

# Developer Info Data
DEVELOPER = {
    "name": "Orukami Orukami! (heck naw im gonna give u my real name)",
    "title": "Indie Game Developer & Designer, ORIGAMIST??",
    "bio": "pls help im losin brian cells",
    "skills": ["Python / Flask", "JavaScript / HTML5", "Pygame", "Godot", "Pixel Art / Pixilart"],
    "github": "https://github.com/programexy",
}

@app.route("/")
def home():
    # Show featured games on the homepage
    featured_games = GAMES[:2]
    return render_template("index.html", games=featured_games)

@app.route("/games")
def games_page():
    # Show all games on the games page
    return render_template("games.html", games=GAMES)

@app.route("/about")
def about_page():
    # Show developer info on the about page
    return render_template("about.html", dev=DEVELOPER)

if __name__ == "__main__":
    app.run(debug=True)