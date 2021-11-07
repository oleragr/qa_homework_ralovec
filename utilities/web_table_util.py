class WebTable:
    def __init__(self, web_table):
        self.table = web_table

    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.table.find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(),
                "columns": self.get_column_count()}

    def get_table_headers(self):
        return self.table.find_elements_by_xpath("//thead/tr[1]/th")

    def get_column_number_by_header(self, header_value):
        headers = self.get_table_headers()
        for header in headers:
            if header.text == header_value:
                return headers.index(header) + 1
        raise Exception("Header was not found!")

    def get_cell_by_column_header(self, row_number, column_header):
        column_number = self.get_column_number_by_header(column_header)
        return self.get_cell(row_number, column_number)

    def get_cell(self, row_number, column_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        cell = self.table.find_element_by_xpath(
            "//tr[" + str(row_number) + "]/td[" + str(column_number) + "]")
        return cell

    def get_cell_data(self, row_number, column_number):
        return self.get_cell(row_number, column_number).text

    def get_cell_position_by_text(self, text):
        table_size = self.get_table_size()
        for i in range(1, table_size.get('rows')):
            for j in range(1, table_size.get('columns')):
                data = self.get_cell_data(i, j)
                if data == text:
                    return i, j
