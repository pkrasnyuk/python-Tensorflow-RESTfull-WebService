import json
import os

from app_config.configuration import Configuration


def load_configuration(config_file_path):
    if config_file_path and os.path.isfile(config_file_path):
        with open(config_file_path, "r") as config_file:
            try:
                load_result = json.dumps(json.load(config_file))
                return __obj_creator(json.loads(load_result))
            except Exception as e:
                print(e)

    return __obj_creator(None)


def __obj_creator(json_object):
    config_host = None
    config_port = 0
    config_logging_name = None
    config_logging_file = None

    if json_object is not None:

        if "app" in json_object and "host" in json_object["app"]:
            config_host = json_object["app"]["host"]

        if "app" in json_object and "port" in json_object["app"]:
            config_port = int(json_object["app"]["port"])

        if "logging" in json_object and "loggingName" in json_object["logging"]:
            config_logging_name = json_object["logging"]["loggingName"]

        if "logging" in json_object and "loggingFile" in json_object["logging"]:
            config_logging_file = json_object["logging"]["loggingFile"]

        return Configuration(
            host=config_host, port=config_port, logging_name=config_logging_name, logging_file=config_logging_file
        )


def __main():
    config_file_path = "../config.json"
    print(load_configuration(config_file_path))


if __name__ == "__main__":
    __main()
