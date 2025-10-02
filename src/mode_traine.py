import os
import sys
import numpy as np
from dataclasses import dataclass
from sklearn.ensemble import RandomForestRegressor
from utils import save_object, evaluate_model
from exception import CustomException
from logger import logging


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")

            X_train, y_train, X_test, y_test = (
                train_array[:, 1:],  # features (excluding first col = target)
                train_array[:, 0],   # target (first column)
                test_array[:, 1:],   # features
                test_array[:, 0]     # target
            )

            logging.info("Training Random Forest Regressor")
            model = RandomForestRegressor(random_state=42, n_estimators=100)

            scores = evaluate_model(model, X_train, y_train, X_test, y_test)

            logging.info(f"Model Evaluation Scores: {scores}")

            # Save model
            os.makedirs(os.path.dirname(self.model_trainer_config.trained_model_file_path), exist_ok=True)
            save_object(self.model_trainer_config.trained_model_file_path, model)

            return scores

        except Exception as e:
            raise CustomException(e, sys)

    

