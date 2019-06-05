from cerberus import Validator


class Degrees:
    __values = []
    __need_relearning = False

    __values_schema = {'type': 'list', 'required': True, 'empty': False}
    __need_relearning_schema = {'type': 'boolean', 'required': False}

    __schema_post = {'values': __values_schema, 'need_relearning': __need_relearning_schema}

    __validator = Validator()

    def __init__(self, values=None, need_relearning=False):
        if values is None:
            values = []

        self.__values = values
        self.__need_relearning = need_relearning

    @classmethod
    def post_instance(cls, json_object):
        validation_result = cls.__validator.validate(document=json_object, schema=cls.__schema_post)
        if not validation_result:
            raise ValueError(cls.__validator.errors)

        values = json_object['values'] if json_object is not None and 'values' in json_object else None
        need_relearning = json_object['need_relearning'] if json_object is not None and 'need_relearning' in json_object else False

        return cls(values=values, need_relearning=need_relearning)


    @property
    def values(self):
        return self.__values

    @property
    def need_relearning(self):
        return self.__need_relearning