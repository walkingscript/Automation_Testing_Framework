from framework.settings.const import BROWSERS


class BrowserIsNotSupported(Exception):
    def __init__(self):
        self.message = f"Supported browsers are {', '.join(BROWSERS)}"


class MethodDoesNotSupportThisLocator(Exception):
    def __init__(self, locator_type):
        self.message = f'Method "find_all" supports only XPATH locator.\nYou uses "{locator_type}".'
