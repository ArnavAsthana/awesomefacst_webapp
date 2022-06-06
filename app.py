from flask import Flask, render_template
from main import Fact

app = Flask(__name__)

@app.context_processor
def add_imports():
    # Note: we only define the top-level module names!
    return dict(Fact=Fact)

@app.route('/')
def Home():
    #Home.render(Fact)
    return render_template("index.html")

app.run(debug=True)