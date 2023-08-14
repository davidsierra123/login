from db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template , url_for

routes_home = Blueprint("routes_home", __name__)

@routes_home.route("/salir" ,  methods=['GET'] )
def exit():
    return render_template('inicio.html')

@routes_home.route("/menu" ,  methods=['GET'] )
def menu():
    return render_template('/main/menu.html')