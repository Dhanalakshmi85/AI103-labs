import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

endpoint = os.getenv("AZURE_ENDPOINT")
key = os.getenv("AZURE_KEY")
name = os.getenv("MY_NAME")

print("Hello", name)
print("Endpoint:", endpoint)
print("Key starts with:", key[:4] + "****")  # never print the full key!