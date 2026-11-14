from azure.ai.textanalytics import TextAnalyticsClient
from azure.identity import DefaultAzureCredential

endpoint = "https://foundry-ai103-dhana.cognitiveservices.azure.com/"
client = TextAnalyticsClient(endpoint=endpoint, credential=DefaultAzureCredential())

docs = [
    "I love studying Azure AI, the labs are amazing!",
    "My name is Anna Virtanen, call me at +358 40 123 4567 or anna@example.com.",
    "Microsoft has a big office in Helsinki.",
]

print("=== 1. SENTIMENT ===")
for doc in client.analyze_sentiment(docs):
    if not doc.is_error:
        print(doc.sentiment, doc.confidence_scores)

print("\n=== 2. PII REDACTION ===")
for doc in client.recognize_pii_entities(docs):
    if not doc.is_error:
        print("Redacted:", doc.redacted_text)
        for e in doc.entities:
            print("  found:", e.text, "->", e.category)

print("\n=== 3. ENTITY LINKING ===")
for doc in client.recognize_linked_entities(docs):
    if not doc.is_error:
        for e in doc.entities:
            print(e.name, "->", e.url)