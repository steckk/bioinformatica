from bioinformatica.source.experiments.models.models_libraries import *
from bioinformatica.source.experiments.models.models_functions import *

from sklearn.metrics import accuracy_score, balanced_accuracy_score, roc_auc_score, average_precision_score


build_models = {
    'SVM': build_SVM,
    'DecTree': build_DecisionTree,
    'RandForest': build_RandomForest,
    'NN': build_NeuralNetwork
}

metrics = [
    accuracy_score,
    balanced_accuracy_score,
    roc_auc_score,
    average_precision_score
]


class Model:
    def __init__(self, type, isNN, training_set, test_set, training_parameters=None):
        self.__type = type
        self.__is_NN = isNN
        self.__training_set, self.__test_set = training_set, test_set
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

    def accuracy(self):
        for metric in metrics:
            self.__scores.append(metric(self.__test_set[-1], test_model(self.__trained_model, self.__test_set[0])))
        return self.__scores

    def get_type(self):
        return self.__type

    type = property(get_type)

