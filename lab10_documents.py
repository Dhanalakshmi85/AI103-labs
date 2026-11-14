from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.identity import DefaultAzureCredential

endpoint = "https://foundry-ai103-dhana.cognitiveservices.azure.com/"
client = DocumentIntelligenceClient(endpoint=endpoint, credential=DefaultAzureCredential())

invoice_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf"

poller = client.begin_analyze_document("prebuilt-invoice", AnalyzeDocumentRequest(url_source=invoice_url))
result = poller.result()   # long-running job: wait for the result

for doc in result.documents:
    for name in ["VendorName", "CustomerName", "InvoiceId", "InvoiceDate", "InvoiceTotal"]:
        field = doc.fields.get(name)
        if field:
            print(f"{name}: {field.content}  (confidence {field.confidence:.2f})")