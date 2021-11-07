import pytest
from pages.herokuapp_page import HerokuappPage
from pages.globalsqa_page import GlobalSqaPage


@pytest.mark.usefixtures("setUp")
class TestHomeworkWeb:

    @pytest.fixture(autouse=True)
    def function_setup(self):
        print("Setting up test")
        self.driver = self.driver
        self.herokuapp_page = HerokuappPage(self.driver)
        self.globalsqa_page = GlobalSqaPage(self.driver)

    def test_herokuapp(self):
        self.herokuapp_page.navigate_to_page()
        self.herokuapp_page.highlight_cell_by_position(3, column_header='Diceret')
        self.herokuapp_page.highlight_link_by_text_in_row('Apeirian7', 'delete')
        self.herokuapp_page.highlight_link_by_text_in_row('Apeirian2', 'edit')
        self.herokuapp_page.highlight_cell_by_text('Definiebas7')
        self.herokuapp_page.highlight_cell_by_text('Iuvaret7')
        self.herokuapp_page.click_green_button()

    def test_globalsqa(self):
        self.globalsqa_page.navigate_to_page()
        self.globalsqa_page.close_iframe_dialog_box()
        images_count = self.globalsqa_page.get_cover_images_count()
        self.globalsqa_page.input_search(images_count)
