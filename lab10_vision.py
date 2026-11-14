from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.identity import DefaultAzureCredential

endpoint = "https://foundry-ai103-dhana.cognitiveservices.azure.com/"
client = ImageAnalysisClient(endpoint=endpoint, credential=DefaultAzureCredential())

image_url = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"

result = client.analyze_from_url(
    image_url=image_url,
    visual_features=[VisualFeatures.OBJECTS, VisualFeatures.TAGS, VisualFeatures.READ],
)
print("\n=== OBJECTS ===")
for obj in result.objects.list:
    print(obj.tags[0].name, obj.bounding_box)
print("=== TAGS ===")
for tag in result.tags.list:
    print(tag.name, f"{tag.confidence:.2f}")

print("\n=== TEXT (OCR) ===")
for block in result.read.blocks:
    for line in block.lines:
        print(line.text)