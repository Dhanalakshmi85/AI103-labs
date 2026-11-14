import json
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)
client = AzureOpenAI(
    azure_endpoint="https://foundry-ai103-dhana.openai.azure.com/",
    azure_ad_token_provider=token_provider,
    api_version="2024-10-21",
)

# The JSON schema: the exact shape we want back
schema = {
    "type": "object",
    "properties": {
        "customer_name": {"type": "string"},
        "product": {"type": "string"},
        "sentiment": {"type": "string", "enum": ["positive", "neutral", "negative"]},
        "needs_reply": {"type": "boolean"},
    },
    "required": ["customer_name", "product", "sentiment", "needs_reply"],
    "additionalProperties": False,
}

review = "Hi, I'm Mikko. My new coffee machine stopped working after 2 days. Please help!"

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "Extract information from customer reviews."},
        {"role": "user", "content": review},
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {"name": "review_info", "strict": True, "schema": schema},
    },
)

data = json.loads(response.choices[0].message.content)   # text -> Python dict
print(json.dumps(data, indent=2))
print("\nCustomer:", data["customer_name"])
print("Needs reply?", data["needs_reply"])