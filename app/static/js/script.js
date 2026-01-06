document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('message');
    const sendBtn = document.querySelector('#chat-input button:last-child');
    const voiceBtn = document.getElementById('voice-btn');

    // Send on Enter
    if (messageInput) {
        messageInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage(getAgent());
            }
        });
    }

    // Voice input
    if (voiceBtn && ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window)) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
        recognition.lang = 'de-DE'; // German
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            messageInput.value = transcript;
            sendMessage(getAgent());
        };

        recognition.onerror = function(event) {
            console.error('Speech recognition error:', event.error);
        };

        window.startVoiceInput = function() {
            recognition.start();
            voiceBtn.textContent = '🎙️';
            voiceBtn.disabled = true;
            setTimeout(() => {
                recognition.stop();
                voiceBtn.textContent = '🎤';
                voiceBtn.disabled = false;
            }, 5000);
        };
    } else if (voiceBtn) {
        voiceBtn.style.display = 'none';
    }
});

function getAgent() {
    // Determine agent based on current page
    const path = window.location.pathname;
    if (path.includes('innenausbau')) return 'innen';
    if (path.includes('aussenarbeiten')) return 'aussen';
    if (path.includes('elektro')) return 'elektro';
    if (path.includes('projektleitung')) return 'projekt';
    return 'innen'; // default
}

function sendMessage(agent) {
    const messageInput = document.getElementById('message');
    const message = messageInput.value.trim();
    if (!message) return;

    // Add user message to chat
    addMessage(message, 'user');

    // Clear input
    messageInput.value = '';

    // Send to server
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message, agent: agent })
    })
    .then(response => response.json())
    .then(data => {
        addMessage(data.response, 'bot');
    })
    .catch(error => {
        addMessage('Fehler: ' + error.message, 'bot');
    });
}

function addMessage(text, type) {
    const messagesDiv = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message ' + type;
    messageDiv.textContent = text;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Carousel functionality
let currentImageIndex = 0;
const images = [
    '/static/images/luxury1.png',
    '/static/images/luxury2.png',
    '/static/images/electro1.png'
];

function changeImage(direction) {
    currentImageIndex += direction;
    if (currentImageIndex < 0) currentImageIndex = images.length - 1;
    if (currentImageIndex >= images.length) currentImageIndex = 0;
    document.getElementById('carousel-image').src = images[currentImageIndex];
}