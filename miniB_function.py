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

# 1. YOUR function (pretend it reads a database)
def get_order_status(order_id):
    orders = {"A100": "shipped", "A200": "processing"}
    return orders.get(order_id, "not found")

# 2. Describe the function to the model (JSON schema again!)
tools = [{
    "type": "function",
    "function": {
        "name": "get_order_status",
        "description": "Get the delivery status of an order by its ID",
        "parameters": {
            "type": "object",
            "properties": {"order_id": {"type": "string"}},
            "required": ["order_id"],
        },
    },
}]

messages = [{"role": "user", "content": "Where is my order A100?"}]

# 3. First call: the model decides to call the tool
response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages, tools=tools)
msg = response.choices[0].message
call = msg.tool_calls[0]
args = json.loads(call.function.arguments)
print("Model wants to call:", call.function.name, args)

# 4. YOUR code runs the function
result = get_order_status(args["order_id"])
print("Function result:", result)

# 5. Send the result back, the model writes the final answer
messages.append(msg)
messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
final = client.chat.completions.create(model="gpt-4.1-mini", messages=messages, tools=tools)
print("Final answer:", final.choices[0].message.content)