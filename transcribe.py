# Transcribes using Whisper
import whisper
import glob
import os

model = whisper.load_model("base")

# Find the most recent audio file
audio_files = sorted(glob.glob("data/conversation_*.wav"), key=os.path.getmtime, reverse=True)
latest_audio = audio_files[-1] if audio_files else None

if latest_audio:
    print(f"Transcribing: {latest_audio}")
    result = model.transcribe(latest_audio)
    transcript = result["text"]
    
    print("Transcription:")
    print(transcript)
    
    transcript_filename = latest_audio.replace(".wav", ".txt")
    with open(transcript_filename, "w") as f:
        f.write(transcript)
    
    print(f"Transcript saved to: {transcript_filename}")
    
else:
    print("No audio files found for transcription.")