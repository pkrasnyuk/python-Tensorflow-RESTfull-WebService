from app_core import logger
from mLearning import DegreesModel

class MlManager:

    @staticmethod
    def get_degrees(values, need_relearning):
        try:
            model = DegreesModel()
            return model.model_predict(values, need_relearning)
        except Exception as e:
            logger.info(e)

        return None
