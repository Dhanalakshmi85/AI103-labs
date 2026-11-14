import azure.cognitiveservices.speech as speechsdk
from azure.identity import DefaultAzureCredential

endpoint = "https://foundry-ai103-dhana.cognitiveservices.azure.com/"
speech_config = speechsdk.SpeechConfig(token_credential=DefaultAzureCredential(), endpoint=endpoint)

# 1. TEXT -> SPEECH
speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"
audio_out = speechsdk.audio.AudioOutputConfig(filename="hello.wav")
synth = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_out)
result = synth.speak_text_async("Hello Dhanalakshmi. You will pass the AI-103 exam.").get()
print("TTS:", result.reason)

# 2. SPEECH -> TEXT
audio_in = speechsdk.audio.AudioConfig(filename="hello.wav")
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_in)
speechsdk.PhraseListGrammar.from_recognizer(recognizer).addPhrase("Dhanalakshmi")
heard = recognizer.recognize_once_async().get()
print("STT heard:", heard.text)