# Translate MP3 from Spanish to English using Gemini

from google import genai
client = genai.Client()
myfile = client.files.upload(file='/Users/chipmoreno/Downloads/WhatsApp Audio 2025-08-08 at 17.03.13.opus')
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=["Transcribe this audio clip from Spanish to English", myfile]
)
print(response.text)