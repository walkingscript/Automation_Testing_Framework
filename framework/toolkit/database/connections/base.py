from logging import getLogger

from mysql.connector.connection import MySQLConnection

logger = getLogger(__name__)


class SqlConnection:
    connect: MySQLConnection  # + PostgresConnection

    def __del__(self):
        logger.info("Removing %s object. DB connection will be closed automatically.", self.__class__.__name__)
        self.connect.close()

    def __enter__(self):
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info('Closing database connection')
        self.connect.close()

    def execute_query(self, query):
        logger.info('Executing query: %s', query)
        cursor = self.connect.cursor()
        cursor.execute(query)
        return cursor.fetchall()
