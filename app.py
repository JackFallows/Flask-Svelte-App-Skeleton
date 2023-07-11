import os

from flask import Flask, send_from_directory, render_template

template_dir = os.path.dirname(__file__)
template_dir = os.path.join(template_dir, 'client', 'public')
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def base():
    return render_template("index.html")

@app.route("/<path:path>")
def home(path):
    return send_from_directory("client/public", path)

if __name__ == "__main__":
    app.run(debug=True)

