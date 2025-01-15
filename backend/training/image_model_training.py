import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def train_image_model():
    # Prepare the dataset
    train_datagen = ImageDataGenerator(rescale=1.0/255)
    train_generator = train_datagen.flow_from_directory(
        'data/images/train', target_size=(224, 224), batch_size=32, class_mode='binary')

    # Define and train a CNN model
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(train_generator, epochs=10)

    # Save the trained model
    model.save('app/models/image_model.h5')



























#---------------------------------------------------------------------------------------

# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# # Prepare the dataset (ensure you have separate folders for human and AI images)
# train_datagen = ImageDataGenerator(rescale=1.0/255)
# train_generator = train_datagen.flow_from_directory('backend/data/images/train', target_size=(224, 224), batch_size=32, class_mode='binary')

# # Define and train a simple CNN model
# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(64, activation='relu'),
#     tf.keras.layers.Dense(1, activation='sigmoid')
# ])

# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# model.fit(train_generator, epochs=10)

# # Save the trained image model
# model.save('backend/models/image_model.h5')
