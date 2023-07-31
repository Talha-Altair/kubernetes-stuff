from dotenv import load_dotenv
import os

load_dotenv()

MONGO_HOST  = os.environ.get("MONGO_HOST")
MONGO_PORT  = os.environ.get("MONGO_PORT")
MONGO_USER  = os.environ.get("MONGO_USER")
MONGO_PASS  = os.environ.get("MONGO_PASS")
MONGO_DB    = os.environ.get("MONGO_DB")