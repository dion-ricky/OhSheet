from ..utils import range_to_a1

class Worksheet:
    """"""
    def __init__(self, client, index=0, title=None):
        self.client = client
        self.spreadsheet = client.spreadsheet

        if title:
            self._open_with_title(title)
        else:
            self._open_with_index(index)

        # self._attributes = self.worksheet.row_values(1)

    def _open_with_index(self, index):
        """Open worksheet using index

        :param index: The index of the worksheet
        :type index: int

        :returns: Instance of `gspread.models.Worksheet`

        """
        self.worksheet = self.spreadsheet.get_worksheet(index)

    def _open_with_title(self, title):
        """Open worksheet using title

        :param title: The name of the worksheet
        :type title: str

        :returns: Instance of `gspread.models.Worksheet`

        This methods calls `gspread.models.Spreadsheet.worksheet()` function

        """
        self.worksheet = self.spreadsheet.worksheet(title)

    def get_total_col(self):
        return self.worksheet.col_count

    def get_total_row(self):
        return self.worksheet.row_count

    def get_all_values(self, row_start=1, col_start=1):
        total_col = self.get_total_col()
        total_row = self.get_total_row()
        all_column = [[col_start, row_start],[total_col, total_row]]
        raw = self.client.get_values(
                '%s!%s' % (self.worksheet.title, range_to_a1(all_column)),
                params={
                    'valueRenderOption': 'UNFORMATTED_VALUE'
                })
    
        return raw