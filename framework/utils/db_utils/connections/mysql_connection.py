import mysql.connector

import framework.utils.logger
from framework.settings.config import db_config
from framework.utils.logger import logger


# TODO: make base connection class with standard methods which will contains needed method for any connection
class Connection:

    def __init__(self):
        framework.utils.logger.info(f"Creating connection with database {db_config.db_name}.")
        self.connect = mysql.connector.connect(user=db_config.db_user, password=db_config.db_password,
                                               host=db_config.db_host, port=db_config.db_port,
                                               database=db_config.db_name)

    def __enter__(self):
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        framework.utils.logger.info("Closing database connection.")
        self.connect.close()
