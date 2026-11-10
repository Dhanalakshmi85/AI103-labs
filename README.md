# AI-103 Labs: Azure AI Apps and Agents

Hands-on labs while preparing for the **Microsoft AI-103: Developing AI Apps and Agents on Azure** certification.

**Author:** Dhanalakshmi Arunkumar · Full Stack Developer & QA
**Language:** Python 3.12 · **Cloud:** Microsoft Azure / Microsoft Foundry

---

## 🎯 Goal

Build practical skills in:
- Deploying and securing AI models in **Microsoft Foundry**
- Building **generative AI** apps, **RAG** solutions and **AI agents**
- Using Azure AI services for **documents, language, speech and vision**
- Writing secure Python code (keyless authentication, no secrets in code)

---

## 🧪 Labs progress

| # | Lab | Azure service | Status |
|---|-----|---------------|--------|
| 0 | Python setup, venv, first script | Python | ✅ Done |
| 1 | Read a secret with no keys in code | Key Vault + Managed identity / RBAC | ⏳ Planned |
| 2 | Deploy a chat model and call it from Python | Microsoft Foundry | ⏳ Planned |
| 3 | Keyless model call with DefaultAzureCredential | Entra ID + RBAC | ⏳ Planned |
| 4 | RAG: index documents and run a hybrid search | Azure AI Search + embeddings | ⏳ Planned |
| 5 | AI agent with a function tool | Foundry Agent Service | ⏳ Planned |
| 6 | Sentiment analysis and PII redaction | Azure Language | ⏳ Planned |
| 7 | Speech-to-text and text-to-speech | Azure Speech | ⏳ Planned |
| 8 | Extract invoice fields | Document Intelligence | ⏳ Planned |
| 9 | Image caption, OCR and content safety | Azure Vision + Content Safety | ⏳ Planned |

---

## 🔒 Security practices

- Secrets are stored in a local `.env` file and **never committed** (see `.gitignore`)
- Keyless authentication with `DefaultAzureCredential` where possible
- Least-privilege access with Azure RBAC roles
- All Azure resources are deleted after each lab

---

## ▶️ How to run

```bash
git clone https://github.com/Dhanalakshmi85/AI103-labs.git
cd AI103-labs
python3 -m venv .venv
source .venv/bin/activate
pip install requests python-dotenv
python3 hello.py
```

Create a `.env` file for your own Azure settings (not included in this repository).

---

## 📚 Resources

- [Microsoft Learn: AI-103 exam page](https://learn.microsoft.com/credentials/)
- [Microsoft Foundry](https://ai.azure.com)
