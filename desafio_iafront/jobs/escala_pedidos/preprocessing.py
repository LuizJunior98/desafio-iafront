from sklearn import preprocessing
from desafio_iafront.jobs.common import transform

from desafio_iafront.data.saving import save_partitioned


class Preprocessing:

    def __init__(self, result, saida):
        self.result = result
        self.saida = saida

    def normalizer(self):
        # Faz a escala dos valores
        result_scaled = transform(self.result, preprocessing.Normalizer())

        # salva resultado
        save_partitioned(result_scaled, self.saida, ['data', 'hora'])

        self.result = result_scaled

    def standard_scale(self):
        # Faz a escala dos valores
        result_scaled = transform(self.result, preprocessing.StandardScaler())

        # salva resultado
        save_partitioned(result_scaled, self.saida, ['data', 'hora'])

        self.result = result_scaled

    def min_max_scale(self):
        # Faz a escala dos valores
        result_scaled = transform(self.result, preprocessing.MinMaxScaler())

        # salva resultado
        save_partitioned(result_scaled, self.saida, ['data', 'hora'])

        self.result = result_scaled

    def max_abs_scale(self):
        # Faz a escala dos valores
        result_scaled = transform(self.result, preprocessing.MaxAbsScaler())

        # salva resultado
        save_partitioned(result_scaled, self.saida, ['data', 'hora'])

        return result_scaled

    def robust_scale(self):
        # Faz a escala dos valores
        result_scaled = transform(self.result, preprocessing.RobustScaler())

        # salva resultado
        save_partitioned(result_scaled, self.saida, ['data', 'hora'])

        self.result = result_scaled

    def power_transformer(self):
        # Faz a escala dos valores
        result_scaled = transform(self.result, preprocessing.PowerTransformer())

        # salva resultado
        save_partitioned(result_scaled, self.saida, ['data', 'hora'])

        self.result = result_scaled
