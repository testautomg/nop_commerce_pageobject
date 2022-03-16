from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("/Users/admin/Desktop/SDET1/sdet1_nop_commerce_pageobject/configurations/config.ini")
    return config.get(section, key)
