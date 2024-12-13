import whisper
import spacy
import librosa
import soundfile
import os


def load_model():
    return whisper.load_model("base")


def preprocess_audio(input_file, output_file):
    # Load audio
    audio, sr = librosa.load(input_file, sr=None)
    
    # Apply noise reduction and normalization
    audio_filtered = librosa.effects.preemphasis(audio)
    max_amplitude = max(abs(audio_filtered))
    audio_normalized = audio_filtered / max_amplitude
    
    # Save the processed audio
    soundfile.write(output_file, audio_normalized, sr)


def transcibe(model, audio_file):
    processed_file = os.path.join(os.path.dirname(audio_file), 'processed_audio.wav')
    preprocess_audio(audio_file, processed_file)
    audio_data, sr = librosa.load(processed_file, sr=16000)
    result = model.transcribe(audio_data, language="en")
    return result["text"]


def similarity(list_of_cmds, userinput):
    nlp = spacy.load("en_core_web_md")

    # Define predefined commands
    commands = [nlp(cmd) for cmd in list_of_cmds]

    # Process the user input
    user_input = nlp(userinput)

    # Compute similarity with predefined commands
    similarities = [user_input.similarity(cmd) for cmd in commands]

    for i in range(len(commands)):
         print(f"Similarity to {commands[i]}: {similarities[i]}")

    highest_similarity = max(similarities)
    chosen_command = list_of_cmds[similarities.index(highest_similarity)]
    return chosen_command

    


