async function detectText() {
    const text = document.getElementById('text-input').value;
    const response = await fetch('http://127.0.0.1:8000/detect', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    document.getElementById('text-result').innerText = data.message;
}

async function detectImage() {
    const imageInput = document.getElementById('image-input');
    const formData = new FormData();
    formData.append('file', imageInput.files[0]);

    const response = await fetch('http://127.0.0.1:8000/detect_image', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('image-result').innerText = data.message;
}

async function detectBehavior() {
    const behavior = document.getElementById('behavior-input').value;
    const response = await fetch('http://127.0.0.1:8000/detect_behavior', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: behavior })
    });
    const data = await response.json();
    document.getElementById('behavior-result').innerText = data.message;
}
