import os
from logging import getLogger

from framework.logger.initialization import init_logging
from framework.toolkit.config_loader import ConfigLoader
from framework.toolkit.data_provider import BaseJSONDataProvider

# place for loading configuration files
properties_filename = os.getenv('FRAMEWORK_PROPERTIES', 'framework/default_properties.json')
config = ConfigLoader(path=properties_filename, allow_search_in_env_vars=True)

# creating additional directories
properties = BaseJSONDataProvider(properties_filename).data
for param, value in properties.items():
    if not param.endswith('_DIRECTORY'):
        continue
    if os.path.exists(value):
        continue
    os.makedirs(value, exist_ok=True)

# logging initialization
init_logging()
logger = getLogger(__name__)
logger.info('Logging initialization completed')
