from framework.const import SUPPORTED_BROWSERS


class BrowserIsNotSupported(Exception):

    def __init__(self):
        self.message = f"Supported browsers are {', '.join(SUPPORTED_BROWSERS)}"


class MethodDoesNotSupportThisLocator(Exception):

    def __init__(self, locator_type):
        self.message = f'Method "find_all" supports only XPATH locator.\nYou uses "{locator_type}".'
