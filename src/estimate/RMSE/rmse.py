import sys
sys.path.append('../../../')
import ast
import pandas as pd
from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.utils.Source.SourceManager import SourceManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager
from math import log,sqrt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant
from itertools import combinations
from src.models.AIC.aic import aic
from src.models.SimpleLm.SimpleLm import SimpleLm
from src.models.StepWise.StepWise import StepWise
from sklearn.metrics import mean_squared_error



if __name__ == '__main__':
    print("Hello")
    print("=====")


    ratio_splitter = SplitFactory('ratio').generate()
    importer_object = ImporterFactory('csv').generate()
    importer_manager = ImporterManager(importer_object)
    files = [{
        'dir': '../../../data/preprocessed/',
        'files': ['new_covid19.csv']
    }]
    data = importer_manager.exec(files)[0]

    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)

    selected_column_list =['health_expend', 'literacy', 'physicians_density', 'obesity',
           'life_expect', 'h_bed_density', 'imigrate_rate']

    # aic_object = aic()
    # aic_model, aic_predictor, aic_result_df = aic.exec( training , selected_column_list, ['recovery_rate'])

    criteria = {
        'p_value': 0.05
    }

    model = StepWise(criteria)
    stepwise_model, stepwise_predictor, stepwise_result_df = model.exec(training, selected_column_list, ['recovery_rate'])

    model = SimpleLm()
    simple_model, simple_predictor, simple_result_df = model.exec(training, selected_column_list, ['recovery_rate'])


    # print(aic_model)
    print(stepwise_result_df)
    print(simple_model)

    # aic_y_pred = aic_model.predict(testing[aic_predictor])
    # print(aic_y_pred)
    # aic_rms = sqrt(mean_squared_error(testing['recovery_rate'], aic_y_pred))
    # print(aic_rms)

    # ypred = olsres.predict(X)

