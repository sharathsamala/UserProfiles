from flask_restful import Resource, reqparse
from models.user import UserModel
from models.profile import ProfileModel

from traceback import format_exc


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field cannot be blank.'
    )

    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field cannot be blank.'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {
                "message": "A user with username: {0} already exists, Try with different username".format(data['username'])
            }, 400

        user = UserModel(**data)
        user.save_to_db()
        try:
            profile = ProfileModel()
            profile.username = data.get('username')
            profile.first_name = data.get('username')
            profile.save()
            print("Successfully created the basic profile")
        except:
            print(format_exc())
            print("ERROR: Unable to create the basic profile data")
        return {'message': 'User created successfully'}, 201
