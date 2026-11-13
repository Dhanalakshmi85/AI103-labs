from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Sign in with az login, no API key!
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)

client = AzureOpenAI(
    azure_endpoint="https://foundry-ai103-dhana.openai.azure.com/",
    azure_ad_token_provider=token_provider,
    api_version="2024-10-21",
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",          # your DEPLOYMENT name
    messages=[
        {"role": "system", "content": "You are a friendly AI-103 tutor. Answer in 2 sentences."},
        {"role": "user", "content": "What is a managed identity?"},
    ],
    temperature=0.2,
    max_tokens=150,
)

print(response.choices[0].message.content)
print("Tokens used:", response.usage.total_tokens)