# AI-103 Labs: Azure AI Apps and Agents

Hands-on labs while preparing for the **Microsoft AI-103: Developing AI Apps and Agents on Azure** certification.

**Author:** Dhanalakshmi Arunkumar · Full Stack Developer & QA
**Language:** Python 3.12 · **Cloud:** Microsoft Azure / Microsoft Foundry

---

## 🎯 Goal

Build practical skills in:
- Deploying and securing AI models in **Microsoft Foundry**
- Building **generative AI**, **RAG** solutions and **AI agents**
- Using Azure AI services for **language, speech, documents and vision**
- Writing secure Python code with **keyless authentication** (no secrets in code)

---

## 🧪 Labs

| # | Lab | Azure service | File | Status |
|---|-----|---------------|------|--------|
| 1 | Resource group setup | Azure Resource Manager | portal | ✅ Done |
| 2 | Key Vault with RBAC (fixed "access denied" with a data-plane role) | Key Vault + RBAC | portal | ✅ Done |
| 3 | Read a secret with no keys in code | Key Vault + DefaultAzureCredential | `lab03_keyvault.py` | ✅ Done |
| 4 | Deploy gpt-4.1-mini and call it from Python (Entra ID, no API key) | Microsoft Foundry | `lab04_chat.py` | ✅ Done |
| 5 | Guardrails: Prompt Shields (jailbreak), content filters, protected material | Foundry Guardrails | portal | ✅ Done |
| 6 | RAG: embeddings, Azure AI Search index, grounded answers with citations | AI Search + Foundry IQ | `lab06-docs/` | ✅ Done |
| 7 | AI agent with a knowledge base (MCP), instructions, versions, traces | Foundry Agent Service | portal | ✅ Done |
| 8 | Sentiment, PII redaction, entity linking | Azure Language | `lab08_language.py` | ✅ Done |
| 9 | Text-to-speech and speech-to-text, phrase list | Azure Speech | `lab09_speech.py` | ✅ Done |
| 10 | Invoice extraction + image tags and OCR | Document Intelligence + Vision | `lab10_documents.py`, `lab10_vision.py` | ✅ Done |

### Mini-labs (in progress)

| # | Mini-lab | Status |
|---|----------|--------|
| A | Structured outputs (JSON schema) | ⏳ Planned |
| B | Agent with function calling | ⏳ Planned |
| C | Evaluation in Foundry | ⏳ Planned |
| D | Layout model + query fields | ⏳ Planned |
| E | Translator | ⏳ Planned |
| F | SSML voice control | ⏳ Planned |
| G | Image captions + object detection | ⏳ Planned |

---

## 🔒 Security practices

- **Keyless authentication** with `DefaultAzureCredential` and Microsoft Entra ID in every Python lab
- **Least-privilege RBAC** roles at resource scope (Key Vault Secrets Officer, Cognitive Services User, Cognitive Services OpenAI User)
- Secrets stored in Key Vault or a local `.env` file, **never committed** (see `.gitignore`)
- Guardrails with **Prompt Shields** and content filters on model deployments
- Free / pay-per-use tiers used and resources removed after the labs

---

## 💡 Key learnings

- Owning a resource (management plane) does not give access to its data (data plane): a data role is needed
- RAG with grounding returns cited answers and says "I don't know" when the data has no answer
- Default PII detection redacts all categories; filter categories to keep needed information
- Speech recognition substitution errors on names: phrase lists help, Custom Speech fixes them reliably

---

## ▶️ How to run

```bash
git clone https://github.com/Dhanalakshmi85/AI103-labs.git
cd AI103-labs
python3 -m venv .venv
source .venv/bin/activate
pip install openai azure-identity azure-keyvault-secrets azure-ai-textanalytics \
            azure-cognitiveservices-speech azure-ai-documentintelligence azure-ai-vision-imageanalysis
az login
python3 lab04_chat.py
```

Update the endpoints in each file to your own Azure resources. Your account needs the matching RBAC role.

---

## 📚 Resources

- [Microsoft Learn: credentials and exams](https://learn.microsoft.com/credentials/)
- [Microsoft Foundry](https://ai.azure.com)
