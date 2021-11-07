"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import os
import platform
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from configfiles.config import ConfigLoader


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser
        self.conf = ConfigLoader().get_configuration()
        self.driver_dir = os.path.dirname(__file__)

    @staticmethod
    def get_chrome_cap():
        c_cap = DesiredCapabilities().CHROME.copy()
        c_cap['download.prompt_for_download'] = False
        c_cap['directory_upgrade'] = True
        c_cap['plugins.plugins_disabled'] = 'Chrome PDF Viewer'
        return c_cap

    def get_chrome_options(self):
        abs_path = os.path.abspath('.')
        downloads_path = os.path.join(abs_path, '_Download')
        c_options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": downloads_path,
                 "directory_upgrade": True,
                 "local_discovery.notifications_enabled": False,
                 "credentials_enable_service": False,
                 "profile": {
                     "password_manager_enabled": False
                 }}
        c_options.add_experimental_option('prefs', prefs)
        c_options.add_argument('--no-sandbox')
        c_options.add_argument("--disable-gpu")
        c_options.add_argument('--disable-dev-shm-usage')  # overcome limited resource problems
        c_options.add_argument('--log-level=3')  # set log level
        c_options.add_argument('--remote-debugging-port=9222')
        c_options.add_argument('--incognito')
        c_options.add_argument('--ignore-certificate-errors')
        c_options.add_argument("--allow-insecure-localhost")
        c_options.add_argument("--allow-running-insecure-content")
        c_options.add_argument("--homepage=about:blank")
        c_options.add_argument("--dom-automation")
        c_options.add_experimental_option('useAutomationExtension', False)
        c_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        if self.browser == 'chrome-headless':
            c_options.add_argument('--headless')

        return c_options

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = self.get_firefox_driver()
        elif self.browser == "chrome":
            driver = self.get_chrome_driver()
        elif self.browser == "chrome-headless":
            driver = self.get_chrome_driver()
        elif self.browser == "edge":
            driver = self.get_edge_driver()
        else:
            driver = self.get_firefox_driver()
        driver.maximize_window()
        return driver

    def get_chrome_driver(self):
        system = platform.system()
        if system == 'Windows':
            return webdriver.Chrome(executable_path=os.path.join(
                self.driver_dir,
                r"Drivers\chromedriver.exe"), options=self.get_chrome_options())
        elif system == 'Linux':
            return webdriver.Chrome(executable_path="chromedriver",
                                    options=self.get_chrome_options())
        else:
            print("unexpected operating system {}".format(system))
            assert False

    def get_edge_driver(self):
        system = platform.system()
        if system == 'Windows':
            return webdriver.Edge(executable_path=os.path.join(
                self.driver_dir,
                r"Drivers\msedgedriver.exe"))
        elif system == 'Linux':
            return webdriver.Edge(executable_path="msedgedriver")
        else:
            print("unexpected operating system {}".format(system))
            assert False

    def get_firefox_driver(self):
        system = platform.system()
        if system == 'Windows':
            return webdriver.Firefox(executable_path=os.path.join(
                self.driver_dir, r"Drivers\geckodriver.exe"))
        elif system == 'Linux':
            return webdriver.Firefox(executable_path="geckodriver")
        else:
            print("unexpected operating system {}".format(system))
            assert False


