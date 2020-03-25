from werkzeug.security import safe_str_cmp
from flask_restful import Resource
from flask_jwt import jwt_required, current_identity

from models.profile import ProfileModel
from resources.utils import profile_to_json


class Profile(Resource):

    @jwt_required()
    def get(self, username):
        if safe_str_cmp(current_identity.username, username):
            profile = get_profile(username)
            if profile:
                return profile_to_json(profile)
            return {"message": "profile not found.. !"}, 404
        return {"message": "username and auth token user are two different users, "
                           "Please pass the same user's auth token"}, 400

    # def put(self, name):


def get_profile(username):
    return ProfileModel.objects(username=username).order_by('-id').first()
