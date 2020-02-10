class Tuple:
    def __init__(self, data, constraints):
        self.data = data
        self.constraints = constraints
        self.cells = self._get_cells()

        self.primary_key = self._find_primary_key()
    
    def _get_cells(self):
        retr = {}
        
        for constraint in self.constraints:
            for attribute in constraint.attribute_name:
                retr[attribute] = Cell(
                                    self.data[attribute],
                                    constraint
                                )

        return retr

    def _find_primary_key(self):
        for constraint in self.constraints:
            if constraint.is_primary_key():
                return constraint.attribute_name
    
    # def get(self, key):
    #     if self.cells[self.primary_key] == key:
    #         return self

class Cell:
    def __init__(self, value, constraint):
        if constraint.validate_data_type(value):
            self.value = value
            self.constraint = constraint
        else:
            from ..exceptions import DataTypeViolation
            raise DataTypeViolation("%s did not satisfy %s" % (value, constraint.data_type))
