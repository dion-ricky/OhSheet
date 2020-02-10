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