from flask import Flask

app = Flask(__name__)

def tpl(title, html):
    return f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        {html}
    </body>
</html>
"""

@app.route("/")
def hello_world():
    return tpl('Heimasíða' ,'<h1>Heimasíðan</h1>')

@app.route("/afangar")
def hello_world():
    return tpl('Áfangar' ,'<h1>Áfangar</h1>')

@app.route("/afangar/afangi")
def hello_world():
    return tpl('Áfangi' ,'<h1>Áfangi</h1>')

@app.route("/nemendur")
def hello_world():
    return tpl('Nemendur' ,'<h1>Nemendur</h1>')

@app.route("/nemendur/nemandi")
def hello_world():
    return tpl('Nemandi' ,'<h1>Nemandi</h1>')

@app.route("/kennerar")
def hello_world():
    return tpl('Kennarar' ,'<h1>Kennarar</h1>')

@app.route("/um-brautina")
def hello_world():
    return tpl('Um brautina' ,'<h1>Um brautina</h1>')
