import re
from gspread.utils import numericise
from .worksheet import Worksheet
from .constraint import Constraint

class Schema:
    def __init__(self, client, title):
        if not re.search("_schema", title):
            title = '%s%s' % (title, "_schema")
        
        self.worksheet = Worksheet(client, title=title)
        self.data = self.worksheet.get_all_values(col_start=2)

        self._parse_schema_data(self.data)

        self.constraints = [
            Constraint(
                self.attributes[i],
                self.primary_constraint[i],
                self.unique_constraint[i],
                self.foreign_constraint[i],
                self.data_type[i])
            
            for i in range(0, len(self.attributes))
        ]
    
    def _parse_schema_data(self, data):
        self.attributes = data['values'][0]

        self.primary_constraint = data['values'][1]
        
        self.unique_constraint = data['values'][2]

        self.foreign_constraint = data['values'][3]

        self.data_type = data['values'][4]