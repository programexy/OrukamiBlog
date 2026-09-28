from flask import Flask, render_template, send_file, abort
from origami_projects import ORIGAMI_PROJECTS
from games_projects import GAMES
import io
import os
import zipfile
from werkzeug.wsgi import FileWrapper

BASE_DIR = "."  # Base path limiting access for security



app = Flask(__name__)

# Sample Game Data

DEVELOPER = {
    "name": "Orukami",
    "title": "Indie Game Developer & Designer, Origamist",
    "bio": "pls help im losin brian cells",
    "skills": ["Python / Flask", "JavaScript / HTML5", "Pygame", "Godot", "Pixel Art / Pixilart"],
    "github": "https://github.com/programexy",
}
# Sample Origami Data with featured flags
@app.route("/")
def home():
    # Filter projects marked as featured
    featured_origami = [p for p in ORIGAMI_PROJECTS if p.get("featured")]
    featured_games = GAMES[:2]
    return render_template("index.html", featured_origami=featured_origami, games=featured_games)

@app.route('/download/<folder_name>')
def download_any_folder(folder_name):
    # Secure path concatenation to prevent directory traversal
    folder_path = os.path.join(BASE_DIR, folder_name)
    
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        abort(404, description="Folder not found")
        
    memory_file = io.BytesIO()
    
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, folder_path)
                zf.write(full_path, relative_path)
                
    memory_file.seek(0)
    
    return send_file(
        FileWrapper(memory_file), # production safe wrapper
        mimetype='application/zip',
        as_attachment=True,
        download_name=f'{folder_name}.zip'
    )

@app.route("/origami")
def origami_page():
    return render_template("origami.html", projects=ORIGAMI_PROJECTS)

@app.route('/monking')
def monking_page():
    return "<a href='https://programexy.github.io/MonKing'>check htis out</a>"
# Developer Info Data

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