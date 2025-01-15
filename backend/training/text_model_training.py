import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_text_model():
    df = pd.read_csv('data/text_data.csv')

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['text'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, 'backend/models/text_model.pkl')
    joblib.dump(vectorizer, 'backend/models/text_vectorizer.pkl')








# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# import joblib
# import os

# def train_text_model():
#     try:
#         # Load the dataset
#         data_path = 'data/text_data.csv'
#         if not os.path.exists(data_path):
#             raise FileNotFoundError(f"Dataset not found at: {data_path}")
        
#         df = pd.read_csv(data_path)

#         # Ensure required columns exist
#         if 'text' not in df.columns or 'label' not in df.columns:
#             raise ValueError("The dataset must contain 'text' and 'label' columns.")
        
#         # Feature extraction using TF-IDF
#         vectorizer = TfidfVectorizer(stop_words='english')
#         X = vectorizer.fit_transform(df['text'])
#         y = df['label']

#         # Train-test split
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#         # Train a Random Forest model
#         model = RandomForestClassifier()
#         model.fit(X_train, y_train)

#         # Save the trained model and vectorizer
#         model_dir = 'backend/models'
#         os.makedirs(model_dir, exist_ok=True)  # Ensure the models directory exists
#         joblib.dump(model, os.path.join(model_dir, 'text_model.pkl'))
#         joblib.dump(vectorizer, os.path.join(model_dir, 'text_vectorizer.pkl'))

#         print(f"Model and vectorizer successfully saved to: {model_dir}")

#     except FileNotFoundError as e:
#         print(f"Error: {e}")
#     except ValueError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     train_text_model()
