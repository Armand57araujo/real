import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_behavior_model():
    df = pd.read_csv('data/behavior_data.csv')

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['behavior'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, 'app/models/behavior_model.pkl')
    joblib.dump(vectorizer, 'app/models/behavior_vectorizer.pkl')










#---------------------------------------------------------------------------------------
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# import joblib

# # Load behavior data (replace with actual data)
# df = pd.read_csv('backend/data/behavior_data.csv')

# # Feature extraction using TF-IDF (or other methods)
# vectorizer = TfidfVectorizer(stop_words='english')
# X = vectorizer.fit_transform(df['behavior'])
# y = df['label']  # 0: Human behavior, 1: AI behavior

# # Split into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train a classifier
# behavior_clf = RandomForestClassifier()
# behavior_clf.fit(X_train, y_train)

# # Save the trained behavior model and vectorizer
# joblib.dump(behavior_clf, 'backend/models/behavior_model.pkl')
# joblib.dump(vectorizer, 'backend/models/behavior_vectorizer.pkl')
