import os
import json
from collections import abc


class ConfigLoader:
    """
    Loads configuration from json file.
    Object of this class allows work with settings as with attributes 
    of class object.
    """
    
    def __init__(self, path='', obj=None):
        """Config object init."""
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                self.__config = json.load(f)
        else:
            self.__config = obj

    def __repr__(self):
        """Returns a friendly object representation"""
        return str(self.__config)
    
    def __getattr__(self, attr):
        """
        Returns json config value if it doesn't conflict with class attrs.
        """
        if param := os.getenv(attr):
            return param
        if hasattr(self.__config, attr):
            return getattr(self.__config, attr)
        else:
            return ConfigLoader.build(self.__config[attr])

    @classmethod
    def build(cls, obj):
        """Alternative constructor."""
        if isinstance(obj, abc.Mapping):
            return cls(obj=obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


# TODO: here must be only framework configuration
config = ConfigLoader(path=CONFIG_FILE)
db_config = ConfigLoader(path=DATABASE_CONFIG)
api_config = ConfigLoader(path=API_CONFIG)
