"""
ohsheet
~~~~~~~

Google Spreadsheets relational library.
"""
from .config import gsclient
from .client import Client

def connect(spreadsheet_id):
    """Connect to Google Spreadsheet using spreadsheet's key

    :param spreadsheet_id: Google Spreadsheet identifier.
                           Can be found on the document's link.
    :type spreadsheet_id: str

    """
    return Client(spreadsheet_id, gsclient)

