from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("C:/Users/QA/PycharmProjects/demo_Project/configurations/config.ini")
    return config.get(section, key)
