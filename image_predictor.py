from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import pandas as pd

classes = [
    'Banh beo',
    'Banh bot loc',
    'Banh cuon',
    'Banh gio',
    'Banh khot',
    'Banh mi',
    'Banh xeo',
    'Bbq chicken wings',
    'Bun bo Hue',
    'Bun dau mam tom',
    'Bun rieu',
    'Bun thit nuong',
    'Burrito',
    'Ca kho to',
    'Canh chua',
    'Cha gio',
    'Chao long',
    'Cheesecake',
    'Chicken curry',
    'Com tam',
    'Donut',
    'Dumpling',
    'French fries',
    'Fried rice',
    'Garlic bread',
    'Goi cuon',
    'Hamburger',
    'Hu tieu',
    'Mi quang',
    'Omelette',
    'Pad thai',
    'Pancake',
    'Pho',
    'Pizza',
    'Ramen',
    'Roasted duck',
    'Sandwich',
    'Spaghetti',
    'Sushi',
    'Waffle',
]
MODEL_PATH = 'D:/Projects/HealthStarRating/Models/ResNet152V2/fine_tune_model_best.hdf5'

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size = (300,300))
    img = image.img_to_array(img) / 255
    img = np.expand_dims(img, axis = 0)
    return img

def predict_image(image_path):
    img = preprocess_image(image_path)
    model = load_model(MODEL_PATH)
    pred_probs = model.predict(img)[0]
    index = np.argmax(pred_probs)
    probability = np.max(pred_probs)*100
    label = classes[index]
    print(f'|=========== Predicted Class: {label} ===========|')
    print(f'|=========== Probability: {probability} ==========|')
    return label

if __name__ == "__main__":
    pass