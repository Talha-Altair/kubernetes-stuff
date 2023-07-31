from pymongo import MongoClient
import urllib.parse
from settings import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASS, MONGO_DB

client = MongoClient(f'mongodb://{MONGO_USER}:{urllib.parse.quote_plus(MONGO_PASS)}@{MONGO_HOST}:{MONGO_PORT}/')

db = client[MONGO_DB]

coll = db.k8s_coll