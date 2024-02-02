import os

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
EMBEDDING_MODEL_NAME = os.environ.get('EMBEDDING_MODEL', 'sentence-transformers/all-MiniLM-L6-v2')
ASTRA_DB_ID = os.environ.get('ASTRA_DB_ID')
ASTRA_DB_REGION = os.environ.get('ASTRA_DB_REGION')
ASTRA_API_ENDPOINT = os.environ.get('ASTRA_API_ENDPOINT')
ASTRA_DB_KEYSPACE_NAME = os.environ.get('ASTRA_DB_KEYSPACE')
ASTRA_DB_APPLICATION_TOKEN = os.environ.get('ASTRA_DB_APPLICATION_TOKEN')
ASTRA_DB_COLLECTION_NAME = os.environ.get('COLLECTION')
