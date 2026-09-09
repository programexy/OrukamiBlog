from flask import Flask, render_template

app = Flask(__name__)

# Sample Game Data
GAMES = [
    {
        "id": "cyber-runner",
        "title": "Cyber Runner",
        "category": "Action / Sci-Fi",
        "description": "A fast-paced neon runner game where you dodge obstacles and hack corporate servers.",
        "image": "https://picsum.photos/id/1060/600/400",
        "game_url": "https://html5.gamedistribution.com/rvvAS308/a4b854e4881045ca800683050d24c08e/" # Sample HTML5 game
    },
    {
        "id": "pixel-dungeon",
        "title": "Pixel Dungeon Explorer",
        "category": "RPG / Adventure",
        "description": "Explore infinite procedural dungeons, defeat goblins, and collect epic loot.",
        "image": "https://picsum.photos/id/1015/600/400",
        "game_url": "https://html5.gamedistribution.com/rvvAS308/a4b854e4881045ca800683050d24c08e/"
    },
    {
        "id": "astro-shooter",
        "title": "Astro Blaster",
        "category": "Arcade / Shooter",
        "description": "Defend the solar system against incoming waves of alien invaders in vintage 8-bit style.",
        "image": "https://picsum.photos/id/1059/600/400",
        "game_url": "https://html5.gamedistribution.com/rvvAS308/a4b854e4881045ca800683050d24c08e/"
    }
]

@app.route("/")
def home():
    return render_template("index.html", games=GAMES)

if __name__ == "__main__":
    app.run(debug=True)