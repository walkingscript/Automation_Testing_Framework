import json
import os
from collections import abc
from logging import getLogger

logger = getLogger(__name__)


class ConfigLoader:
    """
    Loads configuration from json file.
    Object of this class allows work with settings as with attributes 
    of class object.
    """

    def __init__(self, path='', obj=None, allow_search_in_env_vars=False):
        """
        Configuration object.

        @param path: path to configuration file
        @param obj: service parameter to allow dot notation while accessing attrs
        @param allow_search_in_env_vars: allow searching for ENV variables through the config object
        """

        if os.path.exists(path):
            logger.info('Loading configuration from file "%s"', path)
            with open(path, 'r', encoding='utf-8') as f:
                self.__config = json.load(f)
        else:
            if path:
                logger.error('Configuration path "%s" is not exists. (Working directory is "%s")', path, os.getcwd())

        if not path:
            self.__config = obj

        self.allow_search_in_env_vars = allow_search_in_env_vars

    def __repr__(self):
        """Returns a friendly object representation"""
        return str(self.__config)

    def __getattr__(self, attr):
        """
        Returns value of configuration param if it is exists.
        """
        logger.info('Getting access to param "%s"', attr)
        if self.allow_search_in_env_vars:
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


__all__ = ['ConfigLoader']
