from logging import getLogger
from typing import Collection, Union

from prettytable import PrettyTable

logger = getLogger(__name__)


class DatabaseUtils:

    @staticmethod
    def print_data(data: Collection[tuple], headers: Union[Collection, None] = None):
        logger.info('Output data to stdout')
        data = list(map(lambda x: list(map(str, x)), data))
        tbl = DatabaseUtils.get_data_table(data, headers)
        print('\n', tbl)

    @staticmethod
    def log_data(data: Collection[tuple], headers: Union[Collection, None] = None):
        logger.info('Logging data...')
        tbl = DatabaseUtils.get_data_table(data, headers)
        logger.info('\n' + str(tbl))

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
