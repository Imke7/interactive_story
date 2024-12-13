// Show the permission modal
function showPermissionModal() {
    document.getElementById('permission-modal').style.display = 'flex';
}

// Request permissions
function requestPermissions() {
    // Request microphone permission
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function () {
            // Create an audio element with autoplay and muted attributes
            path = "static/audio_files/start_0.wav";
            const audio = new Audio(path);
            audio.volume = 0; // Mute the audio
            audio.autoplay = true;
            audio.muted = true;

            // Play the audio (it should autoplay silently)
            audio.play()
                .then(() => {
                    alert("Permissions granted! Let's start the story.");
                    window.location.href = "/story";  // Redirect to the story page
                })
                .catch((err) => {
                    alert("Autoplay permission is required to continue.");
                });
        })
        .catch(function (err) {
            alert("Microphone access is needed to continue.");
        });

    // Hide the modal
    document.getElementById('permission-modal').style.display = 'none';
}

// Deny permissions and show an alert
function denyPermissions() {
    alert("Permissions denied. You cannot proceed without granting microphone and autoplay access.");
    document.getElementById('permission-modal').style.display = 'none';
}