from fastapi import FastAPI
from app.routes.ai_detection import router as ai_detection_router
from app.routes.auth import router as auth_router

app = FastAPI()

# Include the routes
app.include_router(ai_detection_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Content Detection App!"}











#---------------------------------------------------------------------------
# # from fastapi import FastAPI, HTTPException
# # from pydantic import BaseModel
# # import joblib
# # from PIL import Image
# # import numpy as np
# # import tensorflow as tf
# # import openai

# # # Initialize FastAPI app
# # app = FastAPI()

# # # Load the trained models
# # text_model = joblib.load('backend/models/text_model.pkl')
# # text_vectorizer = joblib.load('backend/models/text_vectorizer.pkl')
# # image_model = tf.keras.models.load_model('backend/models/image_model.h5')
# # behavior_model = joblib.load('backend/models/behavior_model.pkl')
# # behavior_vectorizer = joblib.load('backend/models/behavior_vectorizer.pkl')

# # # OpenAI API Key
# # openai.api_key = 'your-api-key'

# # class TextInput(BaseModel):
# #     text: str

# # class ImageInput(BaseModel):
# #     image_path: str

# # @app.get("/")
# # def index():
# #     return {"message": "AI Detection API is Running"}

# # @app.post("/detect")
# # def detect_ai(input: TextInput):
# #     text = input.text
# #     vectorized_text = text_vectorizer.transform([text])
# #     prediction = text_model.predict(vectorized_text)
# #     result = "AI-generated" if prediction[0] == 1 else "Human-written"
# #     return {"result": result, "message": f"This text was {result}."}

# # @app.post("/detect_image")
# # def detect_image(input: ImageInput):
# #     img = Image.open(input.image_path)
# #     img = img.resize((224, 224))  # Resize image for model input
# #     img_array = np.array(img) / 255.0
# #     img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
# #     prediction = image_model.predict(img_array)
# #     result = "AI-generated" if np.argmax(prediction) == 1 else "Human-generated"
# #     return {"result": result, "message": f"This image is {result}."}

# # @app.post("/detect_behavior")
# # def detect_behavior(input: TextInput):
# #     behavior_text = input.text
# #     vectorized_behavior = behavior_vectorizer.transform([behavior_text])
# #     prediction = behavior_model.predict(vectorized_behavior)
# #     result = "AI-generated" if prediction[0] == 1 else "Human-generated"
# #     return {"result": result, "message": f"This behavior is {result}."}




