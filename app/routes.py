from flask import Flask, render_template, request, jsonify, redirect, url_for
from app import app
from app.speech_recognition import load_model, transcibe, similarity
from app.static.the_story import story
import os


stt_model = load_model()
current_level = 'start'
choice = None
end_of_level = False

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/story')
def story_page():
    global choice
    if current_level == 'end':
         return render_template('end.html', image = f'static/images/lvl31.jpg')
    if end_of_level: # Load page for ending line
        text = story[current_level]['ending_line'][choice]
        lines = [text]
        
        # Find out what the index of the choice was
        for index, key in enumerate(story[current_level]['ending_line'].keys()):
            if key == choice:
                choice_index = index
                break

        # audio files
        audio_files = [f'static/audio_files/{current_level}_ending_{choice_index}.wav']
        if not os.path.isfile(os.path.join(app.root_path, audio_files[0])):
            print(f"Audio file missing at {audio_files[0]}")
        # Image file
        image_path = f'static/images/{current_level}.jpg'
        if not os.path.isfile(os.path.join(app.root_path, image_path)):
            print(f"Image file missing at {image_path}")
        return render_template('story_page.html', audio_files=audio_files, text_snippets=lines, no_choice = True, image = image_path)
            
    
    # Else, just normal level
    text = story[current_level]['text']
    lines = text.splitlines()
    # audio files
    audio_files = [f'static/audio_files/{current_level}_{i}.wav' for i in range(len(lines))]
    for file in audio_files:
        if not os.path.isfile(os.path.join(app.root_path, file)):
            print(f"Audio file missing at {file}")
    no_choice = False # True if there if the user can not choose at the end.
    if len(story[current_level]['choices']) == 1:
        choice = None # To know that we do not have an 'end of the level'
        no_choice = True
    # Image file
    image_path = f'static/images/{current_level}.jpg'
    if not os.path.isfile(os.path.join(app.root_path, image_path)):
         print(f"Image file missing at {image_path}")
    return render_template('story_page.html', audio_files=audio_files, text_snippets=lines, no_choice = no_choice, image = image_path)


@app.route('/continue')
# Function for when there is no choice, the story continues without user input.
def continue_story():
    global current_level
    global end_of_level
    if choice: # previously, a choice has been made. We're just at the end of the level.
        current_level = story[current_level]['choices'][choice]
    else: # This part of the story never had a choice
        choices = list(story[current_level]['choices'].keys())
        chosen_option = choices[0]
        current_level = story[current_level]['choices'][chosen_option]
        if current_level == 'end':
            end_of_level = False
            return redirect(url_for('end'))
    end_of_level = False
    return redirect(url_for('story_page'))

@app.route('/upload_audio', methods=["GET", "POST"])
def upload_audio():
    
    file = request.files['audio_data']

    if file:
        # Save the file 
        path = os.path.join(app.root_path, 'uploads/user_audio.wav')
        file.save(path)
        text = transcibe(stt_model, path)
        print(f"user is saying: {text}")

        # Determine similarity and next nevel
        global choice
        choices = list(story[current_level]['choices'].keys())
        if len(choices) == 1:
            chosen_option = choices[0] # 'no choice' 
        else:
            chosen_option = similarity(choices, text)
            choice = chosen_option

        global end_of_level
        end_of_level = True
        return redirect(url_for('story_page'))
    else:
        return '', 400

@app.route('/end')
def end():
    return render_template('end.html', image = f'static/images/lvl31.jpg')

@app.route('/restart')
def reset():
    global current_level, choice, end_of_level
    current_level = 'start'
    choice = None
    end_of_level = False
    return redirect(url_for('story_page'))