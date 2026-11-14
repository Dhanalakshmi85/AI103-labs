import azure.cognitiveservices.speech as speechsdk
from azure.identity import DefaultAzureCredential

endpoint = "https://foundry-ai103-dhana.cognitiveservices.azure.com/"
speech_config = speechsdk.SpeechConfig(token_credential=DefaultAzureCredential(), endpoint=endpoint)

ssml = """
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
  <voice name="en-US-JennyNeural">
    <prosody rate="slow" pitch="low">Hello Dhanalakshmi.</prosody>
    <break time="1s"/>
    <prosody rate="fast" pitch="high">You will pass the AI-103 exam!</prosody>
  </voice>
</speak>
"""

audio_out = speechsdk.audio.AudioOutputConfig(filename="ssml.wav")
synth = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_out)
result = synth.speak_ssml_async(ssml).get()
print("SSML:", result.reason)