class Tuple:
    def __init__(self, data, constraints, address):
        self.data = data
        self.constraints = constraints
        self.cells = self._get_cells()
        self.address = address

        self.primary_key = self._find_primary_key()
    
    def _get_cells(self):
        from ..utils import cell_addresses_from_range
        retr = {}
        counter = 0
        cell_addresses = cell_addresses_from_range(self.address)

        for constraint in self.constraints:
            retr[constraint.attribute_name] = Cell(
                                self.data[constraint.attribute_name],
                                constraint,
                                cell_addresses[counter]
                            )

            counter += 1

        return retr

    def _find_primary_key(self):
        for constraint in self.constraints:
            if constraint.is_primary_key():
                return constraint.attribute_name
    
    # def get(self, key):
    #     if self.cells[self.primary_key] == key:
    #         return self

class Cell:
    def __init__(self, value, constraint, address):
        if constraint.validate_data_type(value):
            self.value = value
            self.constraint = constraint
            self.address = address
        else:
            from ..exceptions import DataTypeViolation
            raise DataTypeViolation("%s did not satisfy %s" % (value, constraint.data_type))
