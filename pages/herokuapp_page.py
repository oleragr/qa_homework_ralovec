from pages.basepage import BasePage
from utilities.web_table_util import WebTable


class HerokuappPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    Table = 'div.large-10 table'
    EditLink = 'a[href="#edit"]'
    DeleteLink = 'a[href="#delete"]'
    SuccessButton = '[class="button success"]'

    def navigate_to_page(self):
        self.navigateTo(self.conf['base_url_task2'])

    def highlight_cell_by_position(self, row, column=None, column_header=""):
        table = WebTable(self.getElement(self.Table))
        if column:
            cell = table.get_cell(row, column)
        else:
            cell = table.get_cell_by_column_header(row, column_header)
        self.highlightElementForTime(cell)

    def highlight_cell_by_text(self, text):
        table = WebTable(self.getElement(self.Table))
        row, column = table.get_cell_position_by_text(text)
        self.highlight_cell_by_position(row, column)

    def highlight_link_by_text_in_row(self, text, link):
        table = WebTable(self.getElement(self.Table))
        row, column = table.get_cell_position_by_text(text)
        action_column_index = table.get_column_number_by_header("Action")
        cell = table.get_cell(row, action_column_index)
        if link == 'edit':
            link = self.getElement(self.EditLink, parent_element=cell)
        if link == 'delete':
            link = self.getElement(self.DeleteLink, parent_element=cell)
        self.highlightElementForTime(link)

    def click_green_button(self):
        self.elementClick(self.SuccessButton)
