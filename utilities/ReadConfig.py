from configparser import ConfigParser


def read_configuration(category, key, default=None):
    config = ConfigParser()
    try:
        config.read("..//configurations/config.ini")
        if config.has_section(category) and config.has_option(category, key):
            return config.get(category, key)
        else:
            if default is not None:
                return default
            else:
                raise KeyError(f"Category '{category}' or key '{key}' not found in config.ini")
    except Exception as e:
        print(f"An error occurred: {e}")
        return default

# def read_configuration(category, key):
#     config = ConfigParser()
#     config.read("config.ini")
#     return config.get(category, key)
