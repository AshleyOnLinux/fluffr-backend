from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

mUser = os.environ['mongoUsername']
mPass = os.environ['mongoPassword']
mClus = os.environ['mongoCluster']
conn = MongoClient(f"mongodb+srv://{mUser}:{mPass}@{mClus}/?retryWrites=true&w=majority")
