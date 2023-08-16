from flask import Flask, render_template , url_for , session, redirect , request
from db import app
from db import db
from functools import wraps


from Rutas.home import routes_home


app.register_blueprint(routes_home, url_prefix="/fronted")

@app.route("/")
def ini():
    titulo="Pagina principal"
    return render_template('login.html', title=titulo)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')