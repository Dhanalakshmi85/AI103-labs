import requests
from azure.identity import DefaultAzureCredential

# Get a token with az login, no key
token = DefaultAzureCredential().get_token("https://cognitiveservices.azure.com/.default").token

url = "https://foundry-ai103-dhana.cognitiveservices.azure.com/translator/text/v3.0/translate"
params = {"api-version": "3.0", "from": "en", "to": ["fi", "ta"]}
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
body = [{"text": "Good morning! I am studying for the AI-103 exam."}]

response = requests.post(url, params=params, headers=headers, json=body)
print("Status:", response.status_code)

for t in response.json()[0]["translations"]:
    print(f"{t['to']}: {t['text']}")