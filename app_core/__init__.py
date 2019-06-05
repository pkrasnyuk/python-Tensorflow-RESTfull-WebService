import app_config
import helpers

__CONFIG_FILE = "config.json"
config = app_config.load_configuration(__CONFIG_FILE)

logger = helpers.Logger(config.logging_name, config.logging_file).logger_instance