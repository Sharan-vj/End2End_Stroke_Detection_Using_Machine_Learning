# Import Dependencies
from strokePredictor.logging import logger
from strokePredictor.components.model_evaluation import ModelEvaluation
from strokePredictor.config.configuration import ConfigManager

# Stage Name
STAGE_NAME = "MODEL EVALUATION"


# Model Evaluation Pipeline
class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate_model()


if __name__ == '__main__':
    try:
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
    except Exception as e:
        raise e