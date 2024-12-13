const startButton = document.getElementById('go_to_start');

startButton.addEventListener('click', function () {
    fetch('/restart', {
        method: 'GET',
    })
        .then(response => {
            if (response.ok) {
                // Redirect to the story page
                window.location.href = '/story';
            }
        })
        .catch(error => console.error('Error:', error));
});