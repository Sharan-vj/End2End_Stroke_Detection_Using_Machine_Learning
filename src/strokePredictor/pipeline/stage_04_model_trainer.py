# Import Dependencies
from strokePredictor.logging import logger
from strokePredictor.components.model_trainer import ModelTrainer
from strokePredictor.config.configuration import ConfigManager


# Stage Name
STAGE_NAME = "MODEL TRAINING"


# Model Trainer Pipeline
class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train_model()


if __name__ == '__main__':
    try:
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
    except Exception as e:
        raise e