import numpy as np
import tensorflow as tf
import pandas as pd
import pickle

from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.utils import pad_sequences
from sklearn.metrics import accuracy_score, balanced_accuracy_score, confusion_matrix
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense


def preprocess_data(path):
    # load the dataset from the .pkl file
    with open(path, "rb") as file:
        data = pickle.load(file)

    # convert the data into pandas dataframe
    data = pd.DataFrame(data)
    # convert emotions to numbers 0-5
    emotion_mapping = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}
    data["emotions"] = data["emotions"].replace(emotion_mapping)

    x = data["text"].values
    y = data["emotions"].values

    # split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # tokenize the text
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(x_train)
    x_train = tokenizer.texts_to_sequences(x_train)

    # pad the training data
    max_words = 200
    x_train = pad_sequences(x_train, maxlen=max_words)

    y_train = tf.keras.utils.to_categorical(y_train)
    return x_train, y_train, x_test, y_test, tokenizer, max_words


def RNN(x_train, y_train, tokenizer, epochs, batch_size):
    model = Sequential()
    model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64, input_length=x_train.shape[1]))
    model.add(LSTM(64))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(6, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
    return model


# process the test data
def preprocess_test_data(x_test, tokenizer, max_words):
    x_test = tokenizer.texts_to_sequences(x_test)
    x_test = pad_sequences(x_test, maxlen=max_words)
    return x_test


# confusion matrix and accuracy
def review_accuracy(y_test, y_pred):
    print(f'confusion matrix:\n {confusion_matrix(y_test, y_pred)}')
    print(f'accuracy: {accuracy_score(y_test, y_pred)}')
    print(f'balanced accuracy: {balanced_accuracy_score(y_test, y_pred)}')


def pred(x_test, model):
    y_pred = model.predict(x_test)
    return np.argmax(y_pred, axis=1)


def to_emotion(user_input, tokenizer, model, max_words):
    x = preprocess_test_data([user_input], tokenizer, max_words)
    y = pred(x, model)
    emotion_mapping = {0: "sadness", 1: "joy", 2: "love", 3: "anger", 4: "fear", 5: "surprise"}
    return emotion_mapping[y[0]]


x_train, y_train, x_test, y_test, tokenizer, max_words = preprocess_data(r"merged_training.pkl")
model = RNN(x_train, y_train, tokenizer, epochs=4, batch_size=64)

x_test = preprocess_test_data(x_test, tokenizer, max_words)

y_pred = pred(x_test, model)

review_accuracy(y_test, y_pred)

print(to_emotion("Hello world!", tokenizer, model, max_words))

