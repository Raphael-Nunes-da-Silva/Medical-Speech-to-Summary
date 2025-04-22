# 🧠 Speech-to-Summary Recorder

This project is a smart, voice-activated recording and summarization tool that captures conversations, transcribes the speech, summarizes it using AI, and uploads the summary to Google Drive. Ideal for meetings, research discussions, interviews, or personal reflections.

---

## 📌 Features

- 🎙️ One-button controlled voice recording
- 🧠 Speech transcription using OpenAI's Whisper
- ✨ Summarization using Transformer-based models (e.g., BART, PEGASUS)
- ☁️ Automatic document creation and upload to Google Drive
- 🍓 Can run autonomously on a Raspberry Pi 5 with a physical button

---

##  🤖  Software Pipeline (Python Side)

1. **Speech Recognition (Transcription)**  
   - [`whisper`](https://github.com/openai/whisper) by OpenAI (works offline, multilingual, supports multiple speakers)  
   - Alternative: Google Speech-to-Text API

2. **Speaker Diarization (Optional)**  
   - [`pyannote-audio`](https://github.com/pyannote/pyannote-audio)  
   - [`resemblyzer`](https://github.com/resemble-ai/Resemblyzer)

3. **Summarization**  
   - Via the `transformers` library (by Hugging Face):  
     - `facebook/bart-large-cnn`  
     - `google/pegasus-xsum`  
     - Or use OpenAI GPT (3.5/4) via the OpenAI API

4. **Save to Google Drive**  
   - Use `pydrive` or the Google Drive API to create and upload a `.txt` or `.docx` summary file automatically



