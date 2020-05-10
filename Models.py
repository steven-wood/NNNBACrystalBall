import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras import backend as K

c = 0.0
def loss(y_actual, y_predicted):
    return K.mean(
        K.square(y_actual - y_predicted))

def sqErrModel():
    return getModel(loss)


def binNoDecorrelation():
    return getModel('binary_crossentropy')

def getModel(loss):

    model = Sequential()
    model.add(Dense(64, activation='relu', input_dim=22))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss=loss,
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    return model