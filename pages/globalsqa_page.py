from pages.basepage import BasePage


class GlobalSqaPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    IFrame = 'div[rel-title="iFrame"]'
    CloseBlueDialogIcon = IFrame + ' a[class="close_img"]'
    PortfolioItems = 'div[id="portfolio_items"]'
    PicHolder = 'div[class="pic_holder"]'
    MainMenu = 'div[id="menu"]'
    SearchInput = 'input[id="s"]'

    FrameName = 'globalSqa'

    def navigate_to_page(self):
        self.navigateTo(self.conf['base_url_task3'])
        self.wait_for_iframe_content()

    def close_iframe_dialog_box(self):
        close_icon = self.wait_for(self.CloseBlueDialogIcon)
        self.webScrollIntoView(close_icon)
        self.elementClick(element=close_icon)

    def get_cover_images_count(self):
        self.switchToFrame(name=self.FrameName)
        portfolio_area = self.getElement(self.PortfolioItems)
        self.webScrollIntoView(portfolio_area)
        images_count = len(self.getElementList(self.PicHolder, parent_element=portfolio_area))
        self.switchToDefaultContent()
        return images_count

    def wait_for_iframe_content(self):
        self.switchToFrame(name=self.FrameName)
        self.wait_for(self.PortfolioItems, timeout=30)
        self.switchToDefaultContent()

    def input_search(self, value):
        self.sendKeys(data=value, locator=self.SearchInput)
