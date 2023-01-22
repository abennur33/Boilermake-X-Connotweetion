import numpy as np
import pickle
from keras.utils import pad_sequences
import keras

def to_emotion(user_input, tokenizer, model, max_words):
    x = tokenizer.texts_to_sequences([user_input])
    x = pad_sequences(x, maxlen=max_words)
    y = model.predict(x)
    y = np.argmax(y, axis=1)
    emotion_mapping = {0: "sadness", 1: "joy", 2: "love", 3: "anger", 4: "fear", 5: "surprise"}
    return emotion_mapping[y[0]]

tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
model = keras.models.load_model('model.h5')

user_input = "I am very sad"
x = to_emotion(user_input, tokenizer, model, 200)
print(x)