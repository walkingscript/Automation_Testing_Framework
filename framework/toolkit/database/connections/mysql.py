from logging import getLogger

import mysql.connector

from .base import SqlConnection

logger = getLogger(__name__)


class MySqlConnection(SqlConnection):

    def __init__(self, host, port, database_name, user, password):
        logger.info("Creating connection with MySQL database")
        self.connect = mysql.connector.connect(host=host, port=port, database=database_name,
                                               user=user, password=password)
