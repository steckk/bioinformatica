from bioinformatica.source.models_builder.models.models_functions import *


build_models = {
    'SVM': build_SVM,
    'DecTree': build_DecisionTree,
    'RandForest': build_RandomForest,
    'NN': build_NeuralNetwork
}


class Model:
    def __init__(self, type, isNN, training_set, test_set, training_parameters=None):
        self.__type = type
        self.__is_NN = isNN
        self.__training_set, self.__test_set = training_set, test_set
        self.__X_test, self.__y_test = self.__test_set
        self.__training_parameters = training_parameters
        self.__model = None
        self.__trained_model = None
        self.__scores = []

    def build(self, parameters):
        self.__model = build_models.get(self.__type)(parameters)

    def train(self):
        if self.__is_NN:
            training_data = (*self.__training_set, *self.__test_set, self.__training_parameters)
            self.__trained_model = train_model(self.__is_NN, self.__model, training_data)
        else:
            self.__trained_model = train_model(self.__is_NN, self.__model, self.__training_set)

    def metrics(self, metric):
        return str(metric), metric(self.__y_test, test_model(self.__trained_model, self.__X_test))

    def get_type(self):
        return self.__type

    type = property(get_type)
