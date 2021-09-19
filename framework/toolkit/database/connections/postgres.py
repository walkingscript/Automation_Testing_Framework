from logging import getLogger

import psycopg2

from .base import SqlConnection

logger = getLogger(__name__)


class PostgresConnection(SqlConnection):

    def __init__(self, host, port, database_name, user, password):
        logger.info("Creating connection with PostgresSQL on host=%s:%s "
                    "with database '%s' as user '%s' with password=%s",
                    host, port, database_name, user, password)
        self.connect = psycopg2.connect(host=host, port=port, database=database_name, user=user, password=password)
