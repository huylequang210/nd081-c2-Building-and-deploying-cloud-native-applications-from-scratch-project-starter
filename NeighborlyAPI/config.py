import os

from bson.objectid import ObjectId
from pymongo import MongoClient


class Config(object):
    MONGO_URL = "mongodb://project2-cosmos:b9NACSssomPPxcusxFFH6zluoR3xlfAJvHnms4JxNCTnnMkfmAQZxWmliZCdT8sI1pzLIg00mRRZACDbxOxvGg==@project2-cosmos.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2-cosmos@"
    MONGO_DB_NAME = "project2-cosmos-db"
