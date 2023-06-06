"""Main Server!! Woohoo!"""

from flask import (Flask, render_template, request, flash, get_flashed_messages, session, redirect, jsonify)

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Renders the homepage"""

    return render_template('homepage.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)