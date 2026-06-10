from configparser import ConfigParser
import os

def get_config(category, key):
    config = ConfigParser()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(
        os.path.dirname(current_dir),
        "Configuration",
        "config.ini"
    )

    print("Config Path:", config_path)

    config.read(config_path)

    print("Sections:", config.sections())

    return config.get(category, key)