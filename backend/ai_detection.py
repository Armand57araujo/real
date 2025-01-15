import joblib
from PIL import Image
import numpy as np
import tensorflow as tf

# Load models
text_model = joblib.load('backend/models/text_model.pkl')
text_vectorizer = joblib.load('backend/models/text_vectorizer.pkl')
image_model = tf.keras.models.load_model('backend/models/image_model.h5')
behavior_model = joblib.load('backend/models/behavior_model.pkl')
behavior_vectorizer = joblib.load('backend/models/behavior_vectorizer.pkl')

# Predict AI-generated text
def predict_ai_text(text):
    vectorized_text = text_vectorizer.transform([text])
    prediction = text_model.predict(vectorized_text)
    return "AI-generated" if prediction[0] == 1 else "Human-written"

# Predict AI-generated image
def predict_ai_image(image):
    img = Image.open(image)
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = image_model.predict(img_array)
    return "AI-generated" if prediction[0][0] > 0.5 else "Human-generated"

# Predict AI-generated behavior
def predict_ai_behavior(behavior_text):
    vectorized_behavior = behavior_vectorizer.transform([behavior_text])
    prediction = behavior_model.predict(vectorized_behavior)
    return "AI-generated" if prediction[0] == 1 else "Human-generated"
