const pausePlayButton = document.getElementById('pause_play');
const skipButton = document.getElementById('skip');
const buttonContainer = document.getElementById('buttonContainer');

let mediaRecorder;
let audioChunks = [];
let isRecording = false;
let waitForRecording = false;
let playing = false;
let currentLine = 0;

pausePlayButton.addEventListener('click', function () {
    const audioPlayer = document.getElementById('audio-player');

    if (playing) {
        audioPlayer.pause();
        playing = false;
    }
    else if (!playing && !waitForRecording) {
        audioPlayer.play();
        playing = true;
    }
});

skipButton.addEventListener('click', function () {
    currentLine = textSnippets.length;
    // Stop audio
    const audioPlayer = document.getElementById('audio-player');
    audioPlayer.pause();
    playing = false;
    // Hightlight last line
    document.querySelectorAll('.line').forEach(line => line.classList.remove('current-line'));
    const currentTextLine = document.getElementById(`line-${currentLine - 1}`);
    currentTextLine.classList.add('current-line');

    playing = false;
    pausePlayButton.disabled = true;
    skipButton.enabled = false;

    if (noChoice) {
        fetch('/continue', {
            method: 'GET',
        })
            .then(response => {
                if (response.ok) {
                    // Redirect to the story page
                    window.location.href = '/story';
                }
            })
            .catch(error => console.error('Error:', error));
    }
    else {
        replaceButtons();
        waitForRecording = true;
    }
});



function replaceButtons() {
    // Remove pause/play and skip button
    buttonContainer.innerHTML = '';

    // add record button
    const recordButton = document.createElement('button');
    recordButton.textContent = 'Start recording';
    recordButton.id = 'record_button';

    buttonContainer.appendChild(recordButton);

    recordButton.addEventListener('click', async function () {
        if (isRecording) {
            const audioBlob = await stopRecording();
            await uploadBlob(audioBlob, 'wav');
            // Replace button with loading symbol
            const spinner = document.createElement('div');
            spinner.classList.add('loading-spinner'); // Add spinner styling class

            // Replace the button with the spinner
            recordButton.replaceWith(spinner);
        }
        else {
            await startRecording();
            waitForRecording = false;
            recordButton.textContent = 'Stop recording';
        }
    });
}


// Function to start recording
async function startRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

        // Initialize the MediaRecorder only if stream is available
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.start();
        isRecording = true; // Set recording state to true
    } catch (error) {
        console.error("Error accessing microphone:", error);
    }
}

// Function to stop recording and process the audio
function stopRecording() {
    return new Promise((resolve) => {
        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            audioChunks = []; // Reset for the next recording
            resolve(audioBlob);
        };

        mediaRecorder.stop();
        isRecording = false; // Reset recording state
    });
}



/**
 * Uploads audio blob to your server
 * @params {Blob} audioBlob - The audio blob data
 * @params {string} fileType - 'mp3' or 'wav'
 * @return Promise<object>
 */
async function uploadBlob(audioBlob, fileType) {
    const formData = new FormData();
    formData.append('audio_data', audioBlob, 'file');
    formData.append('type', fileType || 'mp3');

    fetch('/upload_audio', {
        method: 'POST',
        cache: 'no-cache',
        body: formData  
    })
        .then(response => {
            if (response.ok) {
                // Redirect to the story page
                window.location.href = '/story';
            } else {
                console.error('Upload failed.');
            }
        })
        .catch(error => console.error('Error:', error));
}


// Plays the audio's and selects the text snippets.
document.addEventListener('DOMContentLoaded', function () {
    const audioPlayer = document.getElementById('audio-player');
    currentLine = 0;

    function playCurrentLine() {
        // Remove bold from all lines
        document.querySelectorAll('.line').forEach(line => line.classList.remove('current-line'));

        // Highlight the current line
        const currentTextLine = document.getElementById(`line-${currentLine}`);
        currentTextLine.classList.add('current-line');

        // Set and play the corresponding audio file
        audioPlayer.src = audioFiles[currentLine];
        audioPlayer.play();
        playing = true;
    }

    // Listen for the 'ended' event on the audio player to move to the next line
    audioPlayer.addEventListener('ended', function () {
        currentLine++;
        if (currentLine < textSnippets.length) {
            playCurrentLine();  // Play the next line
        } else {
            playing = false;
            pausePlayButton.disabled = true;
            if (noChoice) {
                fetch('/continue', {
                    method: 'GET',
                })
                    .then(response => {
                        if (response.ok) {
                            // Redirect to the story page
                            window.location.href = '/story';
                        }
                    })
                    .catch(error => console.error('Error:', error));
            }
            else {
                replaceButtons();
                waitForRecording = true;
            }
        }
    });

    // Start the playback for the first line
    playCurrentLine();
});
