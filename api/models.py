from django.db import models

from db_connect import db

users_collection = db['users']

fundraisers_collection = db['fundraisers']

donations_collection = db['donations']
