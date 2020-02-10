import re
from .worksheet import Worksheet
from .schema import Schema
from .tuple import Tuple
from ..utils import value_zipper

class Relation:
    def __init__(self, client, title):
        if re.search("_schema", title):
            raise Exception("Invalid worksheet name")

        self.client = client
        self.worksheet = Worksheet(client, title=title)
        self.data = self.worksheet.get_all_values()
        self.schema = Schema(client, title)
        
        self.tuples = [
            Tuple(
                data,
                self.schema.constraints
            )
            for data in value_zipper(self.data)
        ]
