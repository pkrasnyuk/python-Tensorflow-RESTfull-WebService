from flask import request
from flask_restplus import Namespace, Resource, fields
from controllers import LinearRegressionController

controller = LinearRegressionController()
instance = Namespace('mLearning', description='Machine learning operations')

degrees_model = instance.model('degrees', {
    'values': fields.List(fields.Raw, required=True, description='An array of float values'),
    'need_relearning': fields.Boolean(description='Need Relearning Model')
})

@instance.route('/linearRegressions')
class LinearRegressions(Resource):
    @staticmethod
    @instance.expect(degrees_model)
    def post():
        return controller.degrees_linear_regressions(data=request.json)