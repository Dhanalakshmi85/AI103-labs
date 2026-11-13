from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

vault_url = "https://kv-ai103-dhana-01.vault.azure.net/"

credential = DefaultAzureCredential()   # uses your az login, no key!
client = SecretClient(vault_url=vault_url, credential=credential)

secret = client.get_secret("demo-secret")
print("Secret name:", secret.name)
print("Secret value:", secret.value)