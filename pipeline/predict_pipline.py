import sys
import os
import pandas as pd
from exception import CustomException
from utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            # Load model & preprocessor
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # Transform features
            data_scaled = preprocessor.transform(features)

            # Prediction
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, 
                 F1: float,
                 F2: float,
                 F3: float,
                 F4: float,
                 F5: float,
                 F6: float,
                 F7: float,
                 F8: float,
                 F9: float):
        
        self.F1 = F1
        self.F2 = F2
        self.F3 = F3
        self.F4 = F4
        self.F5 = F5
        self.F6 = F6
        self.F7 = F7
        self.F8 = F8
        self.F9 = F9

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "F1": [self.F1],
                "F2": [self.F2],
                "F3": [self.F3],
                "F4": [self.F4],
                "F5": [self.F5],
                "F6": [self.F6],
                "F7": [self.F7],
                "F8": [self.F8],
                "F9": [self.F9],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
