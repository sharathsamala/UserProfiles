import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db, mongo_db
from security import authenticate, identity
from resources.user import UserRegister
from resources.profile import Profile


app = Flask(__name__)

# User Auth DB configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'

# Mongo db configs
app.config["MONGODB_SETTINGS"] = {
    "DB": "UserProfiles",
    "host": "mongodb+srv://admin:admin123@cloud1-dhhxk.mongodb.net/UserProfiles?retryWrites=true&w=majority"
}
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(UserRegister, "/register")
api.add_resource(Profile, "/profile/<string:username>")


if __name__ == '__main__':
    try:
        os.remove("./data.db")
    except:
        print("Unable to remove the temp db file")

    db.init_app(app)
    mongo_db.init_app(app)
    app.run(port=5000, debug=True)
