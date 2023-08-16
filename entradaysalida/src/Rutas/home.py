from db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template , url_for

routes_home = Blueprint("routes_home", __name__)

@routes_home.route("/salir" ,  methods=['GET'] )
def exit():
    return render_template('inicio.html')

@routes_home.route("/registro" ,  methods=['GET'] )
def registro():
    return render_template('/main/registro.html')


@routes_home.route("/login" ,  methods=['GET'] )
def login():
    return render_template('/main/login.html')