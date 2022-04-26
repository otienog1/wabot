import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    load_dotenv(find_dotenv())

    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    #     'SQLALCHEMY_DATABASE_URI'
    # )
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv(
    #     'SQLALCHEMY_TRACK_MODIFICATIONS'
    # )

    # db.init_app(app)

    from .wabotbp import wabotpb as wa_blueprint
    app.register_blueprint(wa_blueprint)

    # from .visabp import visabp as visa_blueprint
    # app.register_blueprint(visa_blueprint)

    # from .forex import forex as forex_blueprint
    # app.register_blueprint(forex_blueprint)

    return app

#   from app import db, create_app
#   db.create_all(app=create_app())
#   db.drop_all(app=create_app())

# ssh -i "C:\Users\7plus8\.ssh\3cxkepair-VA.pem" ubuntu@ec2-3-85-72-145.compute-1.amazonaws.com
# ssh -i "C:\Users\7plus8\.ssh\3cxkepair-VA.pem" ubuntu@3.85.72.145
# mysql
# username: mpesa_root
# pass: fWB9TgCoZ49htwHY1uphzNjxgTB3LMb8tNoxI
