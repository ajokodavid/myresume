from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return make_response(render_template("index.html"))

if __name__ == "__main__":
    app.run()