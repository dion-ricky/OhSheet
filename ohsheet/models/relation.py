import re
from .worksheet import Worksheet
from .schema import Schema
from .tuple import Tuple
from ..utils import value_zipper, tuple_range_generator

class Relation:
    def __init__(self, client, title):
        if re.search("_schema", title):
            raise Exception("Invalid worksheet name")

        self.client = client
        self.worksheet = Worksheet(client, title=title)
        self.data = self.worksheet.get_all_values()
        self.schema = Schema(client, title)
        
        self.tuples = self._get_tuples()

    def _get_tuples(self):
        retr = []
        counter = 0

        for data in value_zipper(self.data):
            retr.append(
                Tuple(
                    data,
                    self.schema.constraints,
                    tuple_range_generator(counter, self.data['range'])
                )
            )
            counter += 1
        
        return retr
