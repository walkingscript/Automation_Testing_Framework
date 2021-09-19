import logging
import re


class CredentialsFilter(logging.Filter):
    PATTERN = r'(password|pwd|keys?)\s?=\s?(?P<value>[\w]+)'

    def __init__(self):
        super(CredentialsFilter, self).__init__()
        self.regex = re.compile(self.PATTERN, re.IGNORECASE)

    def filter(self, record):
        record.msg = self.regex.sub('*', record.msg)
        return True
