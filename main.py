# main.py
from record import record_audio
from transcribe import transcribe_audio
from summarize import summarize_text
from upload_drive import upload_summary

print("Recording...")
record_audio()

print("Transcribing...")
text = transcribe_audio("data/conversation.wav")

print("Summarizing...")
summary = summarize_text(text)

print("Uploading to Drive...")
upload_summary(summary)

print("Done!")
