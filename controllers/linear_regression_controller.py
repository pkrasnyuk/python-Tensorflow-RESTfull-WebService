from flask import Response, json

from managers.ml_manager import MlManager
from models.degrees_model import Degrees


class LinearRegressionController:
    __manager = None

    def __init__(self):
        self.__manager = MlManager()

    def degrees_linear_regressions(self, data):
        try:
            degrees_data = Degrees.post_instance(data)
            result = (
                self.__manager.get_degrees(degrees_data.values, degrees_data.need_relearning)
                if self.__manager is not None
                else None
            )

            return (
                Response(response=json.dumps({"result": result.tolist()}), mimetype="application/json", status=200)
                if result is not None
                else Response(response=json.dumps({"message": "No result"}), mimetype="application/json", status=500)
            )
        except ValueError as e:
            return Response(json.dumps({"message": e}), mimetype="application/json", status=422)
        except Exception:
            return Response(json.dumps({"message": "Bad Request"}), mimetype="application/json", status=400)
