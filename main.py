import os
from pymongo import MongoClient

try:
    with MongoClient(
        os.environ["MONGODB_URI"],
        serverSelectionTimeoutMS=10000
    ) as client:
        client.admin.command("ping")
        print("MongoDB conectado com sucesso!")
except Exception as e:
    print("Erro:", type(e).__name__)
