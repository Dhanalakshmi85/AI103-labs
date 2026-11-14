from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, DocumentAnalysisFeature
from azure.identity import DefaultAzureCredential

endpoint = "https://foundry-ai103-dhana.cognitiveservices.azure.com/"
client = DocumentIntelligenceClient(endpoint=endpoint, credential=DefaultAzureCredential())
url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf"

# 1. LAYOUT: text + tables + structure
layout = client.begin_analyze_document("prebuilt-layout", AnalyzeDocumentRequest(url_source=url)).result()
print("Pages:", len(layout.pages), "| Tables:", len(layout.tables or []))
if layout.tables:
    t = layout.tables[0]
    print(f"First table: {t.row_count} rows x {t.column_count} columns")

# 2. INVOICE + QUERY FIELDS: add extra fields with no training
inv = client.begin_analyze_document(
    "prebuilt-invoice",
    AnalyzeDocumentRequest(url_source=url),
    features=[DocumentAnalysisFeature.QUERY_FIELDS],
    query_fields=["ServiceAddress", "PaymentTerms"],
).result()

fields = inv.documents[0].fields
print("\nInvoiceTotal:", fields["InvoiceTotal"].content)
for name in ["ServiceAddress", "PaymentTerms"]:
    f = fields.get(name)
    print(f"{name} (query field):", f.content if f else "not found")