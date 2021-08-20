import os
import shutil

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from framework.core.errors import BrowserIsNotSupported
from framework.settings.config import config
from framework.settings.const import FIREFOX_OPTIONS, CHROME_OPTIONS
from framework.utils.data_provider import BaseJSONDataProvider


class Driver:

    def __init__(self):
        # todo: config that in framework prefs
        self._download_dir = os.path.abspath(config.get('downloads_path', 'downloads'))
        if not os.path.exists(self._download_dir):
            os.makedirs(self._download_dir)

    # todo: remove and rewrite
    def __del__(self):
        if os.path.exists(self._download_dir):
            shutil.rmtree(self._download_dir)


class ChromeDriver(Driver):

    def __init__(self):
        super().__init__()
        self.chrome_settings = BaseJSONDataProvider(CHROME_OPTIONS).data
        self.options = ChromeOptions()
        self.preferences = {}
        self.init_all_arguments()
        self.init_all_preferences()
        self.init_experimental_options()

    def init_all_preferences(self):
        self.__init_default_preferences()
        self.__init_preferences()
        self.options.add_experimental_option('prefs', self.preferences)

    def init_all_arguments(self):
        self.__init_default_arguments()
        self.__init_arguments()

    def __init_default_arguments(self):
        self.options.add_argument(f"--lang={config.locale}")

    def __init_arguments(self):
        for arg in self.chrome_settings['arguments']:
            self.options.add_argument(arg)

    def __init_default_preferences(self):
        # TODO: hard code, move it to chrome prefs
        self.preferences["download.default_directory"] = self._download_dir

    def __init_preferences(self):
        for k, v in self.chrome_settings['preferences'].items():
            self.preferences[k] = v

    def init_experimental_options(self):
        for k, v in self.chrome_settings['experimental_options'].items():
            self.options.add_experimental_option(k, v)

    def create_driver(self):
        return webdriver.Chrome(ChromeDriverManager().install(), options=self.options)


class FirefoxDriver(Driver):

    def __init__(self):
        super().__init__()
        self.options = FirefoxOptions()
        self.init_default_preferences()
        self.init_preferences()

    def init_preferences(self):
        preferences = BaseJSONDataProvider(FIREFOX_OPTIONS).data
        for k, v in preferences.items():
            self.options.set_preference(k, v)

    def init_default_preferences(self):
        # todo: move thar hardcode to firefox prefs
        self.options.set_preference("intl.accept_languages", config.locale)
        self.options.set_preference("browser.download.dir", self._download_dir)

    def create_driver(self):
        return webdriver.Firefox(options=self.options, executable_path=GeckoDriverManager().install())


class WebDriverCreator:

    drivers = {
        'chrome': ChromeDriver(),
        'firefox': FirefoxDriver()
    }

    @classmethod
    def create_driver(cls):
        browser_name = config.web_browser.lower()
        for name, driver in cls.drivers.items():
            if name in browser_name:
                return driver.create_driver()
        raise BrowserIsNotSupported
