import os
from time import sleep, monotonic

import framework.utils.logger
from framework.utils.logger import logger


class FileManager:

    # todo: I think this can be implemented other way
    @staticmethod
    def file_is_appeared(filepath, timeout):
        """
        Check appearing of indicated file.
        Params:
            Filepath - full path to file.
            Timeout in seconds. By default 3 seconds.
        """
        logger.info('Check that filepath=%s had appeared', (filepath,))
        t1 = monotonic()
        while monotonic() - t1 < timeout:
            if os.path.exists(filepath):
                return True
            sleep(0.1)
        return False

    @staticmethod
    def remove_files_from_dir(path_dir: str) -> None:
        framework.utils.logger.info(f'Removing files from {path_dir}')
        for item in os.listdir(path_dir):
            filepath = os.path.abspath(
                os.path.join(path_dir, item)
            )
            if os.path.isfile(filepath):
                os.remove(filepath)
