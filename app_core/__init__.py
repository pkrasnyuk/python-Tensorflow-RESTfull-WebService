import app_config
from helpers.logger import Logger

__CONFIG_FILE = "config.json"
config = app_config.load_configuration(__CONFIG_FILE)

logger = Logger(config.logging_name, config.logging_file).logger_instance
