from typing import Collection, Union

from prettytable import PrettyTable

import framework.utils.logger
from framework.utils.logger import logger
from framework.utils.db_utils.connections.mysql_connection import Connection


class DatabaseUtils:

    # todo: this method is not for this class
    @staticmethod
    def execute(query):
        framework.utils.logger.info(f'Executing query \n{query}\n')
        with Connection() as connect:
            cursor = connect.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
        return data

    @staticmethod
    def print_data(data: Collection[tuple], headers: Union[Collection, None] = None):
        framework.utils.logger.info('Output data to stdout')
        data = list(map(lambda x: list(map(str, x)), data))
        tbl = DatabaseUtils.get_data_table(data, headers)
        print('\n', tbl)

    @staticmethod
    def log_data(data: Collection[tuple], headers: Union[Collection, None] = None):
        framework.utils.logger.info('Logging data...')
        tbl = DatabaseUtils.get_data_table(data, headers)
        framework.utils.logger.info('\n' + str(tbl))

    @staticmethod
    def print_and_log(data: Collection[tuple], headers: Union[Collection, None] = None):
        DatabaseUtils.print_data(data, headers)
        DatabaseUtils.log_data(data, headers)

    @staticmethod
    def get_data_table(data: Collection[Union[list, tuple]], headers: Union[Collection, None] = None):
        if not data:
            return None
        pt = PrettyTable()
        if headers:
            pt.field_names = headers
        pt.add_rows(data)
        return pt.get_string()
