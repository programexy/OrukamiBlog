from flask import Flask, render_template

app = Flask(__name__)

# Sample Game Data
GAMES = [
    {
        "id": "bunny-rage",
        "title": "ShooterBunnyRageGame",
        "category": "Platformer / Shooter",
        "description": "It's a bunny. It's a shooter. It's a RAGE GAME???",
        "image": "/static/images/shooterbunnyragegame.png",
        "game_url": "https://programexy.github.io/Shooter-bunny-rage-game/" # Sample HTML5 game
    },
    {
        "id": "aoti",
        "title": "Attack of the Insects",
        "category": "Platformer / Shooter",
        "description": "I know you loved the ShooterBunnyRageGame. Here is the sequel. (don't worry it's not a rage game)",
        "image": "/static/images/aoti.png",
        "game_url": "https://programexy.github.io/aoti"
    },
    {
        "id": "monking",
        "title": "whoops cant tell u about this one yet",
        "category": "Platformer / Adventure",
        "description": "Wowzers. Lions????",
        "image": "/static/images/filedoesnotexist.png",
        "game_url": "womp womp"
    }
]


ORIGAMI_PROJECTS = [
    {
        "id": "crane",
        "title": "Classic Paper Crane (Orizuru)",
        "difficulty": "Intermediate",
        "description": "The iconic Japanese paper crane representing peace, hope, and longevity.",
        "image": "/static/images/crane.jpg",
        "diagram_image": "/static/images/crane_diagram.jpg",
        "video_url": "https://www.youtube.com/embed/KfnyopxdJXQ",
        "steps": [
            "Start with a square piece of paper color-side up.",
            "Fold in half diagonally both ways, then unfold.",
            "Turn paper over and fold in half horizontally and vertically.",
            "Collapse into a Square Base using the existing creases.",
            "Fold left and right edges into the center line to create a kite shape.",
            "Perform a Petal Fold upwards on both sides to complete the Bird Base.",
            "Narrow the legs, fold head and tail up with inside reverse folds, and pull wings gently apart."
        ]
    },
    {
        "id": "jumping-frog",
        "title": "Interactive Hopping Frog",
        "difficulty": "Easy",
        "description": "An action origami model that physically hops when you press down on its back legs.",
        "image": "/static/images/frog.jpg",
        "diagram_image": "/static/images/frog_diagram.jpg",
        "video_url": "https://www.youtube.com/embed/14I9l6kH9_M",
        "steps": [
            "Start with a rectangular sheet of paper or fold square paper in half.",
            "Create a Waterbomb Base on the top half of the sheet.",
            "Fold bottom corners up to meet the nose to form front legs.",
            "Accordion fold the bottom section to form spring-loaded hind legs.",
            "Flip over and press the rear fold to make it jump!"
        ]
    }
]

@app.route("/origami")
def origami_page():
    return render_template("origami.html", projects=ORIGAMI_PROJECTS)

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