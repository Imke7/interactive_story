'''
This script uses Coqui TTS to transcribe the story. For the script to work, the Docker image of TTS must first be started. 
Use the following two commands:
$ docker run --rm -it -p 5002:5002 --entrypoint /bin/bash ghcr.io/coqui-ai/tts-cpu
$ python3 TTS/server/server.py --model_name tts_models/en/vctk/vits
and wait for the server to start. The server has succesfully started if you see the following lines at the end
of the output:
 * Running on all addresses (::)
 * Running on http://[::1]:5002
 * Running on http://[::1]:5002
Now, open a new terminal and run this Python script.
'''

import requests
import os
from urllib.parse import urlencode
from app.static.the_story import story

# Define the TTS server URL
TTS_SERVER_URL = "http://localhost:5002/api/tts"
CONTAINER_NAME = "tts_server"
speaker_id = "p316" # We can still change this, p236, p245 and p316 sounded okay, but I did not listen to them all.
language_id = "en"

# Extract the lines to be stranscribed
lines = {}
for key in story:
    lines.update({key : story[key]["text"]})
    if "ending_line" in story[key]:
        endings = list(story[key]["ending_line"].values())
        lines.update({key + "_ending" : endings})

# Directory to save the audio files
output_dir = "./app/static/audio_files/"
os.makedirs(output_dir, exist_ok=True)

# Loop through each sentence and send a GET request to the TTS server
for key in lines:
    if "ending" not in key:
        text_array = lines[key].splitlines()
    else:
        text_array = lines[key]
    
    for i, sentence in enumerate(text_array):
        audio_path = f"{output_dir}/{key}_{i}.wav"
        if os.path.isfile(audio_path):
            continue # file already exists
        
        # Prepare query parameters with text, speaker_id, and language_id
        params = {
            "text": sentence,
            "speaker_id": speaker_id,
            "language_id": language_id,
            "style_wav": ""  
        }
        # Encode parameters into a URL-safe format
        query_string = urlencode(params)
        url = f"{TTS_SERVER_URL}?{query_string}"

        # Send GET request to TTS server
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the audio file
            with open(audio_path, "wb") as audio_file:
                audio_file.write(response.content)
            print(f"Saved: {audio_path}")
        else:
            print(f"Failed to process sentence {key}_{i}: {response.text}")

