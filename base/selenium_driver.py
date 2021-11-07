import time
from configfiles.config import ConfigLoader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver
        self.driver_backup = self.driver
        self.conf = ConfigLoader().get_configuration()

    def getTitle(self):
        return self.driver.title

    def navigateTo(self, url):
        return self.driver.get(url)

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="css", parent_element=None):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            if parent_element and locator:
                element = parent_element.find_element(byType, locator)
            else:
                element = self.driver.find_element(byType, locator)
            return element
        except:
            raise AssertionError("Element not found with locator: " + locator + " and locatorType: " + locatorType)

    def getElementList(self, locator, locatorType="css", parent_element=None):
        """
         
        Get list of elements
        """
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            if parent_element:
                element = parent_element.find_elements(byType, locator)
            else:
                self.waitForElement(locator, locatorType)
                element = self.driver.find_elements(byType, locator)
            return element
        except:
            raise AssertionError("Element list not found with locator: " + locator +
                                 " and  locatorType: " + locatorType)

    def elementClick(self, locator="", locatorType="css", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.waitForElement(locator, locatorType)
                element = self.getElement(locator, locatorType)
            element.click()
        except:
            raise AssertionError("Cannot click on the element with locator: " + locator +
                                 " locatorType: " + locatorType)

    def sendKeys(self, data, locator="", locatorType="css", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.waitForElement(locator, locatorType)
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
        except Exception as e:
            raise AssertionError("Cannot send data on the element with locator: " + locator +
                                 " locatorType: " + locatorType)

    def waitForElement(self, locator, locatorType="css",
                       timeout=10, pollFrequency=0.5):
        try:
            byType = self.getByType(locatorType)
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            return element
        except TimeoutException:
            raise AssertionError("Element not appeared on the web page with locator: " + locator +
                                 " locatorType: " + locatorType)

    def wait_for(self, locator, parent_element=None, locatorType="css", poll=0.1, timeout=10):
        end_time = time.time() + timeout
        while True:
            try:
                elm = self.getElement(locator, locatorType=locatorType, parent_element=parent_element)
                return elm
            except AssertionError:
                pass
            time.sleep(poll)
            if time.time() > end_time:
                break
        raise Exception(
            'Time out, waiting for {}'.format(locator)
        )

    def highlightElementForTime(self, element, wait_sec=2):
        original_style = element.get_attribute("style")
        self.driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",
                                   element)
        time.sleep(wait_sec)
        self.driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", element, "style",
                                   original_style)

    def scroll_shim(self, elm):
        x = elm.location['x']
        y = elm.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -200);'
        self.driver.execute_script(scroll_by_coord)
        self.driver.execute_script(scroll_nav_out_of_way)

    def webScrollIntoView(self, elm):
        self.scroll_shim(elm)

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):
        """
        Switch to default content

        Parameters:
            None
        Returns:
            None
        Exception:
            None
        """
        self.driver.switch_to.default_content()
