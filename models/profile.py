from mongoengine import IntField, EmbeddedDocument, EmbeddedDocumentField, EmailField, ListField, StringField

from db import mongo_db


class PhoneModel(EmbeddedDocument):
    """
    Model for saving phone numbers
    """
    country_code = StringField(default="+91")
    primary = IntField(min_value=10, max_value=10)
    secondary = IntField(min_value=8, max_value=10)


class ProfileModel(mongo_db.Document):
    """
    Model for basic profile details
    """
    meta = {'collection': 'profiles'}

    username = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField()
    email_id = EmailField()
    profile_img = StringField(default="")
    about_me = StringField(default="")
    resume = StringField(default="")
    enabled_sections = ListField()
    phone = EmbeddedDocumentField(PhoneModel, default=PhoneModel)








