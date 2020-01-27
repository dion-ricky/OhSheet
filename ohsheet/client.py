"""
ohsheet.client
~~~~~~~~~~~~~~

Client class responsible for communicating with gspread API.

"""

class Client:
    """An instance of this class communicates with gspread API.

    :param spreadsheet_id: An identifier used for Google Spreadsheet.
                           Can be found in document's link

    :param client: An instance of `gspread.client.Client` class.
                   This instance will be used to open the spreadsheet.

    """
    def __init__(self, spreadsheet_id, client):
        self.spreadsheet = client.open_by_key(spreadsheet_id)

    def get_metadata(self):
        return self.spreadsheet.fetch_sheet_metadata()

    def get_values(self, range, params=None):
        return self.spreadsheet.values_get(range, params)

    # def __get_all_value(self, row_from, row_to):
    #     _all_column = [[1, row_from],[self.__total_col, row_to]]
    #     raw = self.sheet.values_get(
    #             '%s!%s' % (self.worksheet.title, range_to_a1(_all_column)),
    #             params={
    #                 'valueRenderOption': 'UNFORMATTED_VALUE'
    #             })

    #     return raw

    # def __value_zipper(self, raw):
    #     all_values = []

    #     for value in raw['values']:
    #         all_values.append(
    #             dict(
    #             zip(
    #                 [key for key in self.__attributes],
    #                 [i for i in value]
    #             )))

    #     return all_values