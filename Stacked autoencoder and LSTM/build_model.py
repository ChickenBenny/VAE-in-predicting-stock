from keras.layers import Input, Dense, Conv1D, MaxPooling1D, UpSampling1D, BatchNormalization, LSTM, RepeatVector, Dropout
from tensorflow.keras.models import Sequential
from keras.models import Model
from keras import regularizers

class build_model():
    def init(self, input_shape, encode_shape_1, encode_shape_2, latent_shape):
        self.input_shape = input_shape
        self.encode_shape_1 = encode_shape_1
        self.encode_shape_2 = encode_shape_2
        self.latent_shape = latent_shape

    def build_autoencoder(self):
        input_data = Input(shape = (1, self.input_shape))
        encode_1 = Dense(self.encode_shape_1, activation = 'relu', activity_regularizer=regularizers.l2(0))(input_data)
        encode_2 = Dense(self.encode_shape_2, activation = 'relu', activity_regularizer=regularizers.l2(0))(encode_1)
        encode_3 = Dense(self.latent_shape, activation = 'relu', activity_regularizer=regularizers.l2(0))(encode_2)

        decode_3 = Dense(self.encode_shape_2, activation = 'relu', activity_regularizer=regularizers.l2(0))(encode_3)
        decode_2 = Dense(self.encode_shape_1, activation = 'relu', activity_regularizer=regularizers.l2(0))(decode_3)
        decode_1 = Dense(self.input_shape, activation = 'sigmoid', activity_regularizer=regularizers.l2(0))(decode_2)

        # encode_1 = Dense(10, activation = 'relu', activity_regularizer=regularizers.l2(0))(input_data)
        # decode_1 = Dense(19, activation = 'sigmoid', activity_regularizer=regularizers.l2(0))(encode_1)


        autoencoder = Model(inputs = input_data, outputs = decode_1)
        encoder = Model(input_data, encode_3)

        autoencoder.compile(loss = 'mean_squared_error', optimizer = 'adam')
        autoencoder.summary()
        return autoencoder, encoder

    def build_lstm(self, input_shape):
        input_data = Input(shape = (1, input_shape))
        lstm1 = LSTM(50, return_sequences=True, activity_regularizer = regularizers.l2(0.001), recurrent_regularizer = regularizers.l2(0), dropout = 0.2, recurrent_dropout = 0.2)(input_data)
        perc = Dense(50, activity_regularizer=regularizers.l2(0.005))(lstm1)
        lstm2 = LSTM(50, activity_regularizer = regularizers.l2(0.001), recurrent_regularizer = regularizers.l2(0), dropout = 0.2, recurrent_dropout = 0.2)(perc)
        out = Dense(1, activity_regularizer=regularizers.l2(0.001))(lstm2)
        LSTMmodel = Model(input_data, out)
        LSTMmodel.compile(optimizer="adam", loss="mean_squared_error")
        LSTMmodel.summary()
        return LSTMmodel