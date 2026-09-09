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
        "title": "MonKing! (The Monkey King)",
        "category": "Platformer / Adventure",
        "description": "Wowzers. King of the jungle?? (Wait aren't those lions?)",
        "image": "https://picsum.photos/id/1059/600/400",
        "game_url": "womp womp"
    }
]

@app.route("/")
def home():
    return render_template("index.html", games=GAMES)

if __name__ == "__main__":
    app.run(debug=True)