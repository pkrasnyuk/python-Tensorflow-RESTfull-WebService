from __future__ import absolute_import, division, print_function, unicode_literals

import os

import numpy as np
import tensorflow as tf


class DegreesModel:
    __epochs = 500
    __learning_rate = 0.1
    __model_loss = "mean_squared_error"
    __package_directory = os.path.dirname(os.path.abspath(__file__))
    __model_path = os.path.join(__package_directory, "saved_models", "degrees.model.h5")
    __model_data_x_path = os.path.join(__package_directory, "data", "degrees_x.txt")
    __model_data_y_path = os.path.join(__package_directory, "data", "degrees_y.txt")

    def __init__(self):
        tf.logging.set_verbosity(tf.logging.ERROR)

    def model_predict(self, values, relearning=False):
        if relearning & os.path.isfile(self.__model_path):
            os.remove(self.__model_path)

        if not os.path.isfile(self.__model_path):
            self.__create_model()

        model = tf.keras.models.load_model(self.__model_path)

        return model.predict(values)

    def __create_model(self):
        model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
        model.compile(loss=self.__model_loss, optimizer=tf.keras.optimizers.Adam(self.__learning_rate))

        model.fit(
            np.loadtxt(self.__model_data_x_path, dtype=float),
            np.loadtxt(self.__model_data_y_path, dtype=float),
            epochs=self.__epochs,
            verbose=False,
        )
        model.save(self.__model_path)

        return model
